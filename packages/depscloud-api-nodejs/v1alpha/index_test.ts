describe("v1alpha", () => {
    test("require", () => {
        const schema = require("./index");

        expect(Object.keys(schema)).toMatchSnapshot();
    });
});
