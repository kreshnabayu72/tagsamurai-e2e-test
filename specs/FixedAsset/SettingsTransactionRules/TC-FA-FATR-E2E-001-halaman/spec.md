---
id: TC-FA-FATR-E2E-001-halaman
title: "Halaman Transaction Settings menampilkan tab, bagian, dan nilai per node Category"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.1#r92", "§4.2#b3", "§4.4#r2", "§9.2#b194", "§9.4.2#r19", "§9.5#r4", "§9.5#r11", "§11#r7"]
smoke: []
dependsOn: []
trace:
  "§9.5#r11": 1
  "§9.5#r4": [2, 3, 4, 5]
  "§9.2#b194": [6, 21]
  "§9.4.2#r19": 7
  "§11#r7": 10
  "§4.2#b3": [12, 18]
  "§4.1#r92": [19, 27, 28]
  "§4.4#r2": [20, 24]
coverage:
  web: automated
---

# Halaman Transaction Settings menampilkan tab, bagian, dan nilai per node Category

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Transaction Settings.
- Data:
  - DU-001-1: Category leaf `Pool Car {runId}`, tanpa sub-Category, ada di entitas aktor. Di tab Borrow: Duration unit bernilai sendiri `Hours`, Max duration Inherit, Max extensions bernilai sendiri `2`, Auto-approve when duration ≤ Inherit, field lain Inherit.
- Kondisi:
  - Company default entitas aktor bernilai bawaan: Allow Borrow `Allow`, Duration unit `Days`, Max duration `14`, Max extensions `1`, Transaction timeout `7`, Require approval Borrow `ON`, Self service `OFF`, Auto-approve `ON`, Auto-approve when duration ≤ `3`.
  - Tidak ada user yang memegang Role Transaksi `Approver` untuk transaksi Borrow di Group mana pun.
  - Plan entitas aktor menyediakan Approval Workflow dan semua tab transaksi, dengan level Feature Suite Borrowing `Full`.

## Test Steps

### Tab awal dan nilai bawaan Company default di All categories
1. Verifikasi tab `Borrow` aktif
2. Verifikasi field `Allow Borrow` bernilai `Allow`
3. Verifikasi field `Duration unit` bernilai `Days`
4. Verifikasi field `Max duration` bernilai `14`
5. Verifikasi field `Max extensions` bernilai `1`
6. Verifikasi field `Transaction timeout` bernilai `7`

### Alert Approver tampil di bagian Approval
7. Verifikasi bagian Approval tab `Borrow` menampilkan Alert warning `No one is assigned as Approver for this transaction in any Group. Approval goes to the Group Manager or Total Control.`

### Tab transaksi aktif dipertahankan bila tersedia di node baru
8. Klik tab `Transfer`
9. Ketik Search Sidebar Category Tree `Pool Car {runId}`, tekan Enter
10. Verifikasi Category leaf `Pool Car {runId}` tampil di Sidebar Category Tree
11. Klik Category leaf `Pool Car {runId}`
12. Verifikasi tab `Transfer` aktif
13. Kosongkan kotak Search Sidebar Category Tree, tekan Enter
14. Klik `All categories`

### Tab pertama dipakai bila tab aktif tidak tersedia di node baru
15. Klik tab `Damaged & Missing`
16. Ketik Search Sidebar Category Tree `Pool Car {runId}`, tekan Enter
17. Klik Category leaf `Pool Car {runId}`
18. Verifikasi tab `Borrow` aktif

### Category leaf menampilkan aturan node itu dan All categories menampilkan aturan Company default
19. Verifikasi field `Max duration` menampilkan teks `Inherit — 14 days (from Company default)`
20. Verifikasi field `Max extensions` bernilai `2`
21. Verifikasi field `Transaction timeout` menampilkan teks `Set in All categories: 7 days`
22. Kosongkan kotak Search Sidebar Category Tree, tekan Enter
23. Klik `All categories`
24. Verifikasi field `Max extensions` bernilai `1`

### Teks Inherit Auto-approve when duration ≤ memakai satuan Duration unit tingkat penyimpan nilainya
25. Ketik Search Sidebar Category Tree `Pool Car {runId}`, tekan Enter
26. Klik Category leaf `Pool Car {runId}`
27. Verifikasi field `Duration unit` bernilai `Hours`
28. Verifikasi field `Auto-approve when duration ≤` menampilkan teks `Inherit — 3 days (from Company default)`
29. Kosongkan kotak Search Sidebar Category Tree, tekan Enter
