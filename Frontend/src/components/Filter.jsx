const Filter = (props) => {
    const filter = (e) => {
        if (e.code === 'Enter') props.filter(e.target.value);
    };

    return <input className="form-control form-control-lg" type="text" placeholder="Buscar por nombre" onKeyUp={filter} />;
};

export default Filter;