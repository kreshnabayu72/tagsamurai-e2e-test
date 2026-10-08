---
id: TC-GS-ACTLOG-E2E-040-tab-user-action-populate-opsi-filter-dari-data-log
title: "Tab User Action: Opsi Filter Terpopulasi Dinamis dari Modul Pengirim dan Penanganan Admin Dihapus"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ACTLOG-165
  - TC-GS-ACTLOG-166
  - TC-GS-ACTLOG-167
  - TC-GS-ACTLOG-168
  - TC-GS-ACTLOG-169
coverage:
  web: automated
---

# Tab User Action: Opsi Filter Terpopulasi Dinamis dari Modul Pengirim dan Penanganan Admin Dihapus

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- Terdapat data log User Action dari berbagai modul pengirim

## Test Steps

### Opsi Dinamis dari Modul Pengirim
1. Buka Filter Panel Tab User Action.
2. Verifikasi opsi field Action, Object, Field, Modified By hanya memuat nilai yang muncul pada data tabel saat ini.
3. Verifikasi tidak ada opsi 'None' atau nilai kosong pada seluruh field.
4. Verifikasi opsi Object tepat sama dengan modul GS pengirim ('User', 'General Settings', 'Brand', 'Measurement', 'Position', 'Division').
5. Verifikasi opsi Action mencakup aksi non-CRUD yang terjadi ('Pair TAG', 'Resend Activation Email', 'Permanently Delete').
### Penambahan Opsi Realtime & Retensi Data Dihapus
6. Lakukan aksi oleh admin baru 'Dewi Lestari' di sesi lain (misal membuat Brand baru).
7. Tanpa refresh halaman, buka kembali dropdown Modified By di Tab User Action.
8. Verifikasi nama 'Dewi Lestari' otomatis muncul di daftar opsi.
9. Filter Modified By 'Wulan', lalu hapus akun admin 'Wulan' di modul User.
10. Muat ulang Tab User Action dengan filter aktif, verifikasi data oleh 'Wulan' dan opsinya tetap bertahan di riwayat log.

## Notes

- Vocabulary Action dan Object dimiliki oleh modul produsen dan tercermin otomatis di dropdown filter.
