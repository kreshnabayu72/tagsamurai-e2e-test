---
name: Global Settings Brand
id: suite-global-settings-brand
description: Spec e2e turunan tc-brand.md untuk Global Settings > Master Reference > Brand
executionOrder: 1.0
parallel: false
---

# Suite: Global Settings Brand

Suite ini mencakup tab Brand pada Master Reference: tabel (Search, Filter, Sort, Pagination, Setup Column, Download), Create, Edit, Delete single dan Bulk Delete, Modal Changelog, Brand Detail (Item Type List dan Device SKU List), Role Matrix, Guided Tooltip, pencatatan log di tiga surface, sinkronisasi ke modul konsumen (Fixed Asset, Admin Console Device SKU, All Tags), batas Master Data Count Limit dan Selection Limit, state tenant, serta ketahanan terhadap kegagalan server.

`parallel: false` karena spec mengubah state global (plan, status Client, format tanggal General Settings, capability role, flag Guided Tooltip, batas Client Limit) dan men-seed Population D-01 dengan nama literal. Spec yang menghapus data (Delete, Bulk Delete) dijalankan sesudah spec lain. Setiap spec tetap menyiapkan dan membersihkan datanya sendiri lewat hook dan tidak bergantung pada hasil spec lain.
