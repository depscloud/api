describe("tracker", () => {
    test("require", () => {
        const schema = require("./index");

        expect(Object.keys(schema)).toMatchSnapshot();
    });
});
