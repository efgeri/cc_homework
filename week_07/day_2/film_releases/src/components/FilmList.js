import Film from "./Film";
const FilmList = ({ films }) => {
  return (
    <ul>
      {films.map((film, index) => {
        return (
          <li key={index}>
            <a href={film.url}>
              <h3>{film.name}</h3>
            </a>
          </li>
        );
      })}
    </ul>
  );
};

export default FilmList;
