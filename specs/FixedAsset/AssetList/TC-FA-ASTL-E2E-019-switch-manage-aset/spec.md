---
id: TC-FA-ASTL-E2E-019-switch-manage-aset
title: "Switch Manage Asset saat kuota Available habis"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-15aa"]
smoke: []
dependsOn: []
trace:
  "ASTL-LOGIC-15aa": [6, 7, 8, 10, 15, 16]
anchor: [2]
coverage:
  web: automated
---
# Switch Manage Asset saat kuota Available habis

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Assets > All Assets.
- Data:
  - DU-019-1: Group `Cabang Surabaya {runId}`, Available license `0`.
  - DU-019-2: Group `Cabang Palembang {runId}`, Available license `0`.
  - DU-019-3: Group `Kantor Pusat {runId}`.
  - DU-019-4: aset Active Unmanaged, Asset Name `Scanner Gudang {runId}`, tampil `Scanner Gudang {runId} - 1`, Brand `Zebra`, Model/Type `DS2208`, Category `Peralatan Gudang`, Group `Cabang Surabaya {runId}`, Status `Available, Unmanaged`.
  - DU-019-5: aset Active Unmanaged, Asset Name `Mesin Hitung {runId}`, tampil `Mesin Hitung {runId} - 1`, Brand `Casio`, Model/Type `HR-100RC`, Category `Peralatan Kantor`, Group `Cabang Surabaya {runId}`, Status `Available, Unmanaged`.
  - DU-019-6: aset Active managed Custody `Available`, Asset Name `Laptop Pro 16 {runId}`, tampil `Laptop Pro 16 {runId} - 1`, Brand `Lenovo`, Model/Type `ThinkPad T14`, Category `Peralatan IT`, Group `Cabang Surabaya {runId}`, Status `Available`.
  - DU-019-7: aset Active managed Custody `Borrowed`, Asset Name `Mouse Wireless {runId}`, tampil `Mouse Wireless {runId} - 1`, Brand `Logitech`, Model/Type `M185`, Category `Peralatan IT`, Group `Cabang Surabaya {runId}`, Status `Borrowed`.
  - DU-019-8: aset Active Unmanaged, Asset Name `Kursi Kerja {runId}`, tampil `Kursi Kerja {runId} - 1`, Brand `Ergotec`, Model/Type `Staff 200`, Category `Furniture`, Group `Cabang Surabaya {runId}`, Status `Available, Unmanaged`.
  - DU-019-9: aset Active managed Custody `Available`, Asset Name `Printer Laser {runId}`, tampil `Printer Laser {runId} - 1`, Brand `Brother`, Model/Type `HL-L2375DW`, Category `Peralatan Kantor`, Group `Kantor Pusat {runId}`, Status `Available`.
  - DU-019-10: aset Active Unmanaged, Asset Name `Tablet Inventaris {runId}`, tampil `Tablet Inventaris {runId} - 1`, Brand `Samsung`, Model/Type `Tab A8`, Category `Peralatan IT`, Group `Cabang Palembang {runId}`, Status `Available, Unmanaged`.
  - DU-019-11: aset Active managed Custody `Borrowed`, Asset Name `Meja Rapat {runId}`, tampil `Meja Rapat {runId} - 1`, Brand `Informa`, Model/Type `Oval 8`, Category `Furniture`, Group `Cabang Palembang {runId}`, Status `Borrowed`.
  - DU-019-12: aset Disposed managed, Asset Name `Genset Cadangan {runId}`, tampil `Genset Cadangan {runId} - 1`, Brand `Perkins`, Model/Type `403A-15G2`, Category `Peralatan Listrik`, Group `Cabang Surabaya {runId}`, Status `Disposed`.

## Test Steps

### Hanya aset managed Available pada group yang sama dapat dipilih
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi baris `Laptop Pro 16 {runId} - 1` tampil pada tabel
3. Centang baris `Scanner Gudang {runId} - 1` dan baris `Mesin Hitung {runId} - 1`
4. Klik `Bulk Action`
5. Pilih `Manage`
6. Verifikasi dialog `Switch Manage Asset` memuat baris `Laptop Pro 16 {runId} - 1`
7. Verifikasi dialog tidak memuat baris `Mouse Wireless {runId} - 1` (Borrowed), `Kursi Kerja {runId} - 1` (Unmanaged), `Genset Cadangan {runId} - 1` (Disposed), maupun `Printer Laser {runId} - 1` (group lain)
8. Verifikasi penghitung `0 of 2 selected` dan `[Switch]` `Disabled`
9. Centang baris `Laptop Pro 16 {runId} - 1` di dalam dialog
10. Verifikasi penghitung `1 of 2 selected` dan `[Switch]` tetap `Disabled` karena jumlah terpilih kurang dari jumlah aset yang di-Manage
11. Klik `[Cancel]`
12. Klik `×` pada Bar Bulk

### Group tanpa aset managed pasangan
13. Klik menu `⋯` pada baris `Tablet Inventaris {runId} - 1`
14. Pilih `Manage`
15. Verifikasi dialog `Switch Manage Asset` memuat `No managed assets available` dan `There are no other managed assets in this group to switch with.`
16. Verifikasi `[Switch]` `Disabled` sehingga hanya `[Cancel]` yang dapat dipakai
17. Klik `[Cancel]`
