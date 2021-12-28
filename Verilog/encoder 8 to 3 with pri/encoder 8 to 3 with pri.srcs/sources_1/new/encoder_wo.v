`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 08.12.2021 19:30:58
// Design Name: 
// Module Name: encoder_wo
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module encoder_wo(out_y, in_a);
input [7:0]in_a;
output reg [2:0]out_y;
always@(in_a)
begin
case(in_a)
8'b00000001:out_y = 3'b000;
8'b00000010:out_y = 3'b001;
8'b00000100:out_y = 3'b010;
8'b00001000:out_y = 3'b011;
8'b00010000:out_y = 3'b100;
8'b00100000:out_y = 3'b101;
8'b01000000:out_y = 3'b110;
8'b10000000:out_y = 3'b111;
default:$display("Error!");
endcase
end
endmodule
