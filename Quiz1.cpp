//
// Created by Murilo Matos on 1/22/26.
//
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
///For simplicity we will make a 2d array with a couple of book titles, also used for testing

string booktable[2][2] = {
    {"wizard of oz", "the man and the sea"}, {
        "hunger games", "lola"}};

template <typename T, int col, int row>
vector<T> convert_2d_to_1d(const string (&booktable)[row][col]) {
    vector<T> result;
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            bool found = find(booktable[i].begin(), booktable[i].end(), booktable[i][j]) != booktable[i].end(); ,
            auto it = std::find(booktable.begin(), booktable.end(), booktable[i][j]);
            if (it != booktable[i].end()) {
                result.push_back(booktable[i][j]);
            }

            //Check if this is already in the array or not
        }
    }
}


int main() {
    convert_2d_to_1d<string>(booktable);

};
