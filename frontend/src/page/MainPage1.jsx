import React from "react";
import {
  Table,
  Badge,
  Menu,
  Dropdown,
  Icon,
  Button,
  Divider,
  Typography
} from "antd";

const { Text } = Typography;

const menu = (
  <Menu>
    <Menu.Item>Action 1</Menu.Item>
    <Menu.Item>Action 2</Menu.Item>
  </Menu>
);

class MainPage extends React.Component {
  expandedRowRender = () => {
    const columns = [
      {
        title: "Office Name",
        dataIndex: "name",
        key: "name",
        render: text => <span>{text}</span>
      },
      {
        title: "Street",
        dataIndex: "street",
        key: "street",
        render: text => <span>{text}</span>
      },
      {
        title: "Postal Code",
        dataIndex: "postal_code",
        key: "postal_code",
        render: text => <span>{text}</span>
      },
      {
        title: "City",
        dataIndex: "city",
        key: "city",
        render: text => <span>{text}</span>
      },
      {
        title: "Monthly Rent",
        dataIndex: "monthly_rent",
        key: "monthly_rent",
        render: text => <span>{text}</span>
      },
      {
        title: "Other",
        dataIndex: "tag",
        key: "headquarter",
        render: (value, record) => {
          if (record.headquarter) {
            return <Text mark>Headquarter</Text>;
          }
        }
      },
      {
        title: "Action",
        key: "action",
        render: (text, record) => (
          <span>
            <Button type="danger" disabled>
              Delete
            </Button>
          </span>
        )
      }
    ];

    const data = [];
    for (let i = 0; i < 3; ++i) {
      data.push({
        key: i,
        date: "2014-12-24 23:12:00",
        name: "This is production name",
        upgradeNum: "Upgraded: 56"
      });
    }
    return <Table columns={columns} dataSource={data} pagination={false} />;
  };

  render() {
    const columns = [
      {
        title: "Company Name",
        dataIndex: "name",
        key: "name",
        render: text => <span>{text}</span>
      },
      {
        title: "Street",
        dataIndex: "street",
        key: "street",
        render: text => <span>{text}</span>
      },
      {
        title: "Postal Code",
        dataIndex: "postal_code",
        key: "postal_code",
        render: text => <span>{text}</span>
      },
      {
        title: "City",
        dataIndex: "city",
        key: "city",
        render: text => <span>{text}</span>
      },
      {
        title: "Action",
        key: "action",
        render: (text, record) => (
          <span>
            <Button onClick={() => this.openEditModal(record.id, record.name)}>
              Edit
            </Button>
            <Divider type="vertical" />
            {/* <Button onClick={() => this.officeList(record.name)}>
              Office List
            </Button> */}
            {/* <Divider type="vertical" /> */}
            <Button type="danger" disabled>
              Delete
            </Button>
          </span>
        )
      }
    ];

    const data = [];
    for (let i = 0; i < 3; ++i) {
      data.push({
        key: i,
        name: "Screem",
        platform: "iOS",
        version: "10.3.4.5654",
        upgradeNum: 500,
        creator: "Jack",
        createdAt: "2014-12-24 23:12:00"
      });
    }
    return (
      <>
        <div className="company_header">
          <h1>Company List</h1>
          <Button
            type="primary"
            onClick={() => this.setState({ createModal: true })}
          >
            <Icon type="plus" />
            Create a Company
          </Button>
        </div>
        <Table
          className="components-table-demo-nested"
          columns={columns}
          expandedRowRender={this.expandedRowRender}
          dataSource={data}
        />
      </>
    );
  }
}

export default MainPage;
