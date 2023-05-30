import {Culture} from './models';

function serializeCulture(culture: Culture | Culture[]): any {
  const serializeSingleCulture = (c: Culture) => {
    return {
      ...c.toJSON(),
      imageUrl: c.imageUrl,
    };
  };

  if (Array.isArray(culture)) {
    return culture.map(serializeSingleCulture);
  }

  return serializeSingleCulture(culture);
}

export default serializeCulture;