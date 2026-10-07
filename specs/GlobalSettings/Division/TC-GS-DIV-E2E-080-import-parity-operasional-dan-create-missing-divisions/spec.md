---
id: TC-GS-DIV-E2E-080-import-parity-operasional-dan-create-missing-divisions
title: "Parity Operasional Import Division dan Alur Create Missing Divisions: Mutasi, Pencatatan Changelog, Batas Limit, dan Penolakan Duplicate"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-256
  - TC-GS-DIV-257
  - TC-GS-DIV-289
  - TC-GS-DIV-290
coverage:
  web: automated
---

# Parity Operasional Import Division dan Alur Create Missing Divisions: Mutasi, Pencatatan Changelog, Batas Limit, dan Penolakan Duplicate

## Prerequisites

- Login sebagai Role: Total Control
- Akses modul Import > Import Type Division dan Create Missing Divisions dari User Import
- User berada di Global Settings > User > Division
- Division `Import Division A` dibuat lewat tombol `[Create Missing Divisions]` dari Import User Login (Data Uji Dinamis D-16)
- Division `Import Division B` (TC-GS-DIV-256) dipakai oleh user hasil Import
- Master Data Count Limit entitas diset sama dengan jumlah Division saat ini (Admin Console > Plans & Licensing > Lifecycle Settings > System Limits)
- Staging Table Import User Login memuat baris dengan Division `Limit Import Unit` yang belum ada
- Staging Table Import User Login memuat baris dengan Division `Race Import Unit` yang belum ada saat dibaca
- Admin lain membuat Division `Race Import Unit` lewat `[+ Division]` setelah Staging Table dibaca dan sebelum tombol diklik

## Test Steps

### Division hasil Create Missing Divisions dari Import dapat di-Edit identik dengan Create manual (TC-GS-DIV-256)

1. Buka row action baris `Import Division A` lalu `Edit`
2. Ubah Name menjadi `Import Division B` dan klik `[Save]`
3. Verifikasi Toast sukses: `Success, division has been updated.`
4. Verifikasi Name dan Code ter-update seperti Division hasil Create manual
5. Verifikasi Entri Edit tercatat di Changelog

### Division hasil Create Missing Divisions mengikuti guard in-use dan Delete yang sama (TC-GS-DIV-257)

6. Buka row action baris `Import Division B` lalu `Delete`
7. Verifikasi Dialog `Cannot Delete Data` tampil seperti Division hasil Create manual: `Import Division B — still in use` dan `[OK]`

### Create Missing Divisions saat Master Data Count Limit tercapai ditolak (TC-GS-DIV-289)

8. Buka Global Settings > Import, jalankan Import User Login hingga Staging Table menampilkan Division yang belum ada
9. Klik `[Create Missing Divisions]`
10. Buka Global Settings > User > Division
11. Verifikasi Division `Limit Import Unit` tidak dibuat (limit dihitung atomik saat eksekusi tombol)
12. Verifikasi Baris Tab User terkait tetap berstatus `error` di Staging Table
13. Verifikasi Jumlah Division tidak melebihi limit dan tidak ada entri Create baru di Changelog

### Create Missing Divisions untuk nama yang sudah dibuat pihak lain ditolak sebagai duplicate (TC-GS-DIV-290)

14. Klik `[Create Missing Divisions]` pada Staging Table
15. Buka Global Settings > User > Division dan Modal Changelog
16. Verifikasi Tidak ada Division ganda `Race Import Unit`; Division milik admin lain tidak dipakai ulang
17. Verifikasi Baris Tab User terkait tetap berstatus `error` di Staging Table
18. Verifikasi Changelog hanya memuat 1 entri Create `Race Import Unit` (milik admin lain)

## Notes

- Memvalidasi parity operasional divisi hasil import: divisi hasil Create Missing Divisions dapat diedit dan dihapus mengikuti guard yang sama dengan create manual, penolakan tombol Create Missing Divisions saat Master Data Count Limit tercapai, dan penolakan duplikasi saat nama divisi dibuat pihak lain di waktu bersamaan (PRD §9.5, §9.6, §11, testcase-conventions.md P7).
- Sumber pemetaan test case granular: TC-GS-DIV-256, TC-GS-DIV-257, TC-GS-DIV-289, TC-GS-DIV-290.
