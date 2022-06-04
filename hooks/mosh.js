export default useApi = (api) => {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(false);

    const fetchData = async () => {
        setLoading(true);
        const response = await api();
        setLoading(false);

        if (!response.OK) return setError(true);

        setData(response.data);
        setError(false);
    }

    return { data, loading, error, fetchData };
}