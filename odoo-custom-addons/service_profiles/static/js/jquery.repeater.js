(function ($) {
    $.fn.repeater = function (options) {
        // Default params
        var params = $.extend({
            structure: [],
            items: [],
            repeatElement: 'structure',
            createElement: 'createElement',
            removeElement: 'removeElement',
            containerElement: 'containerElement',
            dangerClass: ' btn btn-danger',
            groupName: 'group'
        }, options);

        var repeater = this;

        repeater.find('#' + params.createElement).click(function () {
            // limit items max to 5
            if (params.items.length >= 0 && params.items.length < 5) {
                var cloned = repeater.find('#' + params.repeatElement).clone();
                var inputs = cloned.find(':input');
                var newItem = [];
                $.each(inputs, function (key, input) {
                    var next = params.items.length;
                    newItem.push({
                        id: $(input).attr('id'),
                        value: ''
                    })
                    $(input).attr('name', params.groupName + '[' + next + '][' + $(input).attr('name') + ']')
                })
                cloned.append('<input type="button" class="' + params.removeElement + params.dangerClass + '" value="remove" />')
                cloned.find('.' + params.removeElement).click(function () {
                    $(this).parent().remove();
                    if (params.onRemove !== undefined) {
                        params.onRemove();
                    }
                })
                cloned.show()
                cloned.appendTo('#' + params.containerElement)
                if (params.onShow !== undefined) {
                    params.onShow();
                }
                params.items.push(newItem)
            }
        });

        if (params.items.length > 0 && params.items.length < 3) {
            $.each(params.items, function (key1, item) {
                var cloned = repeater.find('#' + params.repeatElement).clone();
                var inputs = cloned.find(':input');
                $.each(inputs, function (key2, input) {
                    $(input).attr('name', params.groupName + '[' + key1 + '][' + $(input).attr('name') + ']')
                })
                cloned.append('<input type="button" class="' + params.removeElement + params.dangerClass + '" value="remove" />')
                $.each(item.elements, function (index, element) {
                    cloned.find('#' + element.id).val(element.value)
                })
                cloned.find('.' + params.removeElement).click(function () {
                    $(this).parent().remove();
                    if (params.onRemove !== undefined) {
                        params.onRemove();
                    }
                })
                cloned.show()
                cloned.appendTo('#' + params.containerElement)
            })
        }

    }
}(jQuery));