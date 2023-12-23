const Products = (props) => {
    return (
        <table className="table">
            <thead>
                <tr>
                    <th scope="col">Nombre</th>
                    <th scope="col">Cantidad de mercados</th>
                    <th scope="col">Rango de precio</th>
                </tr>
            </thead>
            <tbody>
                {props.products.map((product) => {
                    return (
                        <tr key={product.Ean.nombre}>
                            <td>{product.Ean.nombre}</td>
                            <td>{product.Ean.markets}</td>
                            <td>{product.Ean.rango}</td>
                        </tr>
                    );
                })}
            </tbody>
        </table>
    );
};

export default Products;