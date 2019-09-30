# Helper functions


def h(elm_type, props='', *args):
    return React.createElement(elm_type, props, *args)


def render(react_element, destination_id, callback=lambda: None):
    container = document.getElementById(destination_id)
    ReactDOM.render(react_element, container, callback)


useState = React.useState
useEffect = React.useEffect
useRef = React.useRef


def useInterval(func, delay):
    ref = useRef(func)
    ref.current = func

    def setup():
        id = setInterval(lambda: ref.current(), delay)
        return lambda: cleanInterval(id)

    useEffect(setup, [delay])


# Create a component

def Hello(props):
    count, setCount = useState(0)

    def updateCounter():
        setCount(count+1)

    useInterval(updateCounter, 1000)

    return h(
        'div',
        {'className': 'maindiv'},
        h('h1', None, 'Hello ', props['name']),
        h('p', None, 'Lorem ipsum dolor sit ame.'),
        h('p', None, 'Counter: ', count),
        h(
            'button',
            {'onClick': updateCounter},
            'Increment',
        )
    )


# Render the component in a 'container' div

element = React.createElement(Hello, {'name': 'React!'})
render(element, 'container')
