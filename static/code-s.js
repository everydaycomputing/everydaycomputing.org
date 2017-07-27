var elements = [];
var type = 0;
$(function() {
  console.log(elements)
  // on dom ready
  var cy = cytoscape({
    container: document.getElementById("cy"),

    boxSelectionEnabled: false,
    autounselectify: true,

    elements: elements,

    layout: {
      name: "breadthfirst",
      directed: true,

      padding: 100,
      //name: 'preset',
      fit: true,
      avoidOverlap: true,
      avoidOverlapPadding: 150,
      spacingFactor: 1.8
    },

    ready: function() {
      window.cy = this;
    },

    style: [
      {
        selector: "edge",
        style: {
          width: "4",
          "target-arrow-shape": "triangle",
          "curve-style": "bezier",
          "control-point-step-size": 40,
          label: "data(label)",
          "font-family": "liberation-sans, sans-serif",
          "font-weight": "600",
          "font-size": "60"
        }
      },
      {
        selector: "node",
        style: {
          shape: "roundrectangle",
          "text-wrap": "wrap",
          "text-max-width": 225,
          "text-valign": "center",
          "font-family": "liberation-sans, sans-serif",
          "font-weight": "600",
          "font-size": "17",
          "border-width": "4px 0px 4px 0px",
          height: 250,
          width: 250,
          padding: 10,
          label: "data(name)"
        }
      },
      {
        selector: "node.beginning",
        style: {
          // "border-width": 4,
          "border-color": "green",
          "border-style": "solid"
        }
      },
      {
        selector: "node.intermediate",
        style: {
          // "border-width": 4,
          "border-color": "orange",
          "border-style": "solid"
        }
      },
      {
        selector: "node.advanced",
        style: {
          // "border-width": 4,
          "border-color": "purple",
          "border-style": "solid"
        }
      },
      {
        selector: "node.unplugged",
        style: {
          "background-color": "#c6c6c6",
          color: "#0169D9"
        }
      },
      {
        selector: "node.programming",
        style: {
          "background-color": "white"
        }
      }
    ]
  });

  function rotate() {
    setTimeout(function() {
      cy.nodes().positions(function(node, i) {
        return {
          x: node.position("y") * 0.8,
          y: -1 * node.position("x") * 0.7
        };
      });
      cy.fit();
    }, 100);
  }
  rotate();

  cy.contextMenus({
    menuItems: [
      {
        id: "action_lgs",
        content: "Action Learning Goals",
        selector: "node",
        onClickFunction: function(event) {
          var target = event.target || event.cyTarget;
          // target.data("name", target.data("algs"));
          // cy
          //   .style()
          //   .selector(target)
          //   .style({
          //     "font-size": "60"
          //     // 'background-color': 'yellow'
          //   })
          //   .update();
          // var win = window.open(target.data("href")[0]["link"]);
          // if (!win) {
          //   alert("Please allow popups");
          // }
          // target.style({'font-size': "17"});
        }
      },
      {
        id: "understanding_lgs",
        content: "Understanding Learning Goals",
        selector: "node",
        onClickFunction: function(event) {
          var target = event.target || event.cyTarget;
          // target.data("name", target.data("ulgs"));
          // target.style({'font-size': "17"});
          // console.log(target.position("y"));
          // cy
          //   .style()
          //   .selector(target)
          //   .style({
          //     "font-size": "60"
          //     // 'background-color': 'yellow'
          //   })
          //   .update();
          // var win = window.open(target.data("href")["url"]);
          // if (!win) {
          //   alert("Please allow popups");
          // }
        }
      },
      {
        id: "arrow_activities",
        content: "Arrow Activities",
        selector: "edge",
        onClickFunction: function(event) {
          var target = event.target || event.cyTarget;
          // target.data("label", target.data("source"));
        }
      }
    ]
  });

  var advancedButton = document.getElementById("advanced");
  advancedButton.addEventListener("click", function() {
    cy.$("*").show();
  });

  var intermediateButton = document.getElementById("intermediate");
  intermediateButton.addEventListener("click", function() {
    cy.$("*").show();
    cy.$(".advanced").hide();
  });

  var beginningtButton = document.getElementById("beginning");
  beginningtButton.addEventListener("click", function() {
    cy.$("*").show();
    cy.$(".advanced").hide();
    cy.$(".intermediate").hide();
  });

  cy.nodes().on("mouseover", function() {
    cy
      .style()
      .selector(this)
      .style({
        "border-color": "black",
        "border-width": "7px"
        // 'background-color': 'yellow'
      })
      .update(); // update the elements in the graph with the new style
  });
  cy.nodes().on("mouseout", function() {
    cy
      .style()
      .selector(this)
      .style({
        "border-color": function(node) {
          if (node.hasClass("beginning")) {
            return "green";
          } else if (node.hasClass("intermediate")) {
            return "orange";
          } else {
            return "purple";
          }
        },
        "border-width": "4px"
        // 'background-color': 'yellow'
      })
      .update(); // update the elements in the graph with the new style
  });


  cy.nodes().on("click", function() {
    //   cy.style()
    //     .selector(this)
    //     .style({
    //       'border-color' : 'black'
    //     // 'background-color': 'yellow'
    //   })

    // .update() // update the elements in the graph with the new style
    function fn1(node) {
      function fn_x(node) {
        return node.renderedPosition("x");
      }
      function fn_y(node) {
        return node.renderedPosition("y");
      }
      if (node.data("clicked_var") == 1) {
        node.data("clicked_var", 0);
        // document.getElementById("my-btn").style.visibility = "hidden";
        cy
          .style()
          .selector(node)
          .style({
            "font-size": "17"
            // 'background-color': 'yellow'
          })
          .update();
        return node.data("temp_name");
      } else {
        var collection = cy.nodes();
        function get_name(ele) {
          return ele.data("temp_name");
        }
        collection.map(function change_name(ele) {
          ele.data("name", get_name(ele));
          cy
            .style()
            .selector(ele)
            .style({
              "font-size": "17"
            })
            .update();
        });
        node.data("clicked_var", 1);
        // document.getElementById("my-btn").style.visibility = "visible";
        // document.getElementById("my-btn").style.border = "solid";
        // document.getElementById("my-btn").style.borderColor = "black";
        // document.getElementById("my-btn").style.border = "solid";
        // document.getElementById("my-btn").style.borderWidth = "2px";
        // console.log("x :" + fn_x(node));
        // document.getElementById("my-btn").style.left = 47 + fn_x(node) + "px"; //548 + fn_x(node) * 0.546 + "px";//fn2(node) + "px";
        // console.log("y :" + fn_y(node));
        // document.getElementById("my-btn").style.top = 50 + fn_y(node) + "px"; //40 + fn_y(node) * -0.546 + "px";
        cy
          .style()
          .selector(node)
          .style({
            "font-size": "80"
            // 'background-color': 'yellow'
          })
          .update(); // update the elements in the graph with the new style
        return node.data("id");
      }
    }
    this.data({ name: fn1(this) });

    // window.open('http://maroonstack.com')

    //   cy.$('node:selected').neighborhood('edge').style({
    //   'line-color': 'black'
    // }); console.log('hi');
  });

}); // on dom ready

// function clear_elements() {
//   elements = { nodes: [], edges: [] };
// }

// function accept_data(input) {
//   // input = JSON.parse(input);
//   // console.log(input);
//   alert(input);
//   if (type == 0) {
//     type = 1;
//     for (node in input[0]) {
//       var data = node.data; //["data"];
//       var id = data.id; //data["id"];
//       var name = data.name; //data["name"];
//       var temp_name = name;
//       var clicked_var = 0;
//       var href = [];
//       var classes = node.classes; //node["classes"];
//       var grabbable = false;
//       data = {
//         id: id,
//         clicked_var: clicked_var,
//         temp_name: temp_name,
//         name: name,
//         href: href
//       };
//       elements[nodes].append({
//         data: data,
//         grabbable: grabbable,
//         classes: classes
//       });
//     }
//   } else {
//     type = 0;
//     for (arrow in input[1]) {
//       var data = arrow.data; //["data"];
//       var label = data.data; //["label"];
//       var source = data.source; //["source"];
//       var target = data.target; //["target"];
//       var unplugged = data.unplugged; //["unplugged"];
//       data = {
//         source: source,
//         target: target,
//         label: label,
//         unplugged: unplugged
//       };
//       elements[edges].append({ data: data });
//     }
//   }
// }

function accept_data(input) {
  if(!('classes' in input)) {
    var data = input.data;
    console.log(data)
    var source = data.source;
    var target = data.target;
    var label = data.label;
    var unplugged = data.unplugged;
    console.log(label);
    elements.push({data : {source : source, target : target, label : label, unplugged : unplugged}});
  } else {
    var data = input.data;
    console.log(data);
    var classes = input.classes;
    var id = data.id;
    var name = data.name;
    var temp_name = data.temp_name;
    var clicked_var = data.clicked_var;
    var href = data.href;
    // var classes = class_dict.classes;
    console.log(id);
    elements.push({data : {id : id, temp_name : temp_name, name : name, clicked_var : clicked_var, href : href}, 
      grabbable : false, classes : classes});
  }

}
