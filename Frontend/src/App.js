import { useEffect, useState } from 'react';
import Products from './components/Products';
import Filter from './components/Filter';

function App() {
    const [products, setProducts] = useState([]);
    const [allProducts, setAllProducts] = useState([]);

    const getProducts = async () => {
        let data = await fetch('http://localhost:5000');
        data = await data.json();
        return data;
    };

    const filter = async (text) => {
        const products = allProducts.filter((product) => product.Ean.nombre.toLowerCase().includes(text.toLowerCase()));
        setProducts(products);
    };

    useEffect(() => {
        (async () => {
            const rows = await getProducts();
            setProducts(rows);
            setAllProducts(rows);
        })();
    }, []);

    return (
        <>
            <Filter filter={filter} />
            <br />
            <Products products={products} />
        </>
    );
}

export default App;