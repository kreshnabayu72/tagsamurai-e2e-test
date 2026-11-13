# Usulan Naik ke "Di Dalam Filter": Global Settings > User

Modul: Global Settings > User (User List, User Detail, Modal Changelog, Tab Log)
Sumber tabel: laporan progres e2e, scope `out` (luar filter), `GlobalSettings/User`
Tanggal: 2026-11-13

## Kriteria

Spek dinaikkan ke "di dalam filter" bila dampak bisnisnya tinggi kalau spek itu benar-benar bug, tanpa melihat status run terakhir. Bila spek gagal karena kekurangan helper, spek tetap diusulkan tapi ditandai `helper-gap`, supaya FE tahu naiknya baru berguna setelah helper-nya ada.

## Daftar Usulan Naik

| Spek | Judul | Prioritas | Alasan dampak bisnis | Status run | Helper-gap |
|---|---|---|---|---|---|
| E2E-025 | Create User: Trim Spasi Awal/Akhir First Name, Last Name, Employee ID, dan Email lewat Stay on this form | High | Data tersimpan dengan spasi tidak wajar dan bisa lolos validasi duplikat | Gagal: elemen tidak ditemukan | tidak |
| E2E-026 | Create: nilai khusus, Temporary besok, reuse Email dan Employee ID milik user terhapus | High | Email atau Employee ID user terhapus bisa dipakai ulang atau justru ditolak salah | Gagal: elemen tidak ditemukan | tidak |
| E2E-029 | Create: saving state tombol [Submit] dan klik ganda | High | Klik ganda bisa membuat user ganda | Gagal: elemen tidak ditemukan | tidak |
| E2E-053 | Selection Limit Bulk Action: Checkbox Melewati Batas Disabled, Select All Dibatasi, Nilai Dibaca Live | High | Bulk action bisa melewati batas yang ditetapkan | Gagal: gap terbuka | ya (Selection Limit User tidak bisa diatur lewat helper) |
| E2E-070 | Multi-Konteks Dua Admin: Email Kembar saat Create, Last-Write-Wins, Record Dihapus Sesi Lain | High | Risiko korupsi data saat dua admin bekerja bersamaan | Gagal: nilai atau state beda | tidak |
| E2E-145 | Pencatatan Modal Changelog User > Role: Edit Permission, Assign Role, dan Remove Role | Medium | Jejak audit perubahan hak akses | Gagal: nilai atau state beda | ya (tidak ada kontrak API yang membaca baris role satu user) |
| E2E-148 | Tab User Log: Login, Logout, Change Password, Reset Password, Session started dan ended | Medium | Jejak audit keamanan: login dan perubahan kredensial | Gagal: API backend menolak (login 500) | ya (produk Fixed Asset dan Supply Asset untuk sesi, BT-88) |
| E2E-149 | Tab User Log: Note Lock Change Password 15 Menit, 1 Jam, Perlu Reset, dan Account locked | Medium | Jejak audit kebijakan kunci akun | Gagal: ui-gap terbuka | tidak (ui-gap, bukan helper) |
| E2E-151 | Sinkron Custom Field (Create, Deactivate, Activate, Delete, Ubah Data Type, Required) ke User Existing | Medium | Perubahan custom field yang tidak sinkron ke user yang sudah ada | Gagal: dialog lain menutupi | tidak |
| E2E-156 | State Tenant: Write-Lockdown Client Suspended dan Expired | High | Client suspended atau expired masih bisa menulis data | Gagal: dialog lain menutupi | ya (change-logs tanpa scope objectId; status Expired tidak bisa diatur) |
| E2E-160 | Role Matrix Negatif: Detail User untuk Read Only (Tooltip Checkbox Tab Role, Baris Switch OFF, Keenam Tab Tanpa Kontrol Tulis) | Medium | Hak akses Read Only bocor ke kontrol tulis | Gagal: gap terbuka | ya (baca baris Tab Role satu user; change-logs tanpa scope) |
| E2E-175 | Multi-Konteks: Resend Ditolak saat Cooldown, Switch Tab Role dan Auto-Revert, Deactivate saat User Dihapus Admin Lain | High | Aksi tetap jalan padahal state sudah berubah di sesi lain | Gagal: elemen tidak ditemukan | ya (baca baris Tab Role satu user) |
| E2E-176 | State Tenant Client Suspended: Tab Role Disabled, Resend Hidden, Tooltip Suspended Menang atas Read Only | Medium | Kontrol tulis Client suspended harus terkunci | Gagal: dialog lain menutupi | ya (baca Tab Role; tooltip suspended belum ada di UI) |
| E2E-177 | Multi-Konteks: Concurrent Create Dua Admin pada Slot Master Data Limit Terakhir | Medium | Bug bisa melewati kuota Master Data Limit | Belum ada skrip | tidak |

## Yang Tidak Dinaikkan

- Tab Changelog Detail (E2E-092 sampai 094) dan sub-tab Responsibilities (E2E-116 sampai 136): pola list seragam, dampak bisnis rendah. Keputusan tetap di luar filter.
- Spek kosmetik atau pola list yang sudah dianggap rendah (Guided Tooltip 005 dan 006, foto 027, format tanggal 154, isolasi sub-tab 158, badge kolom 172, paginasi reset 173) tetap di luar filter.
- Pola Search, Filter, Sort, Pagination, Setup Column, dan Download (073 sampai 075, 077, 080 sampai 082, 086 sampai 088, 098 sampai 100, 104 sampai 106, 110 sampai 112) tetap di luar filter.

## Catatan untuk FE

- Spek bertanda `ya` di kolom Helper-gap baru bisa lulus setelah helper yang disebut tersedia. Sebelum itu, naiknya tetap sah sebagai daftar, tapi run-nya akan gagal.
- Spek dengan status "dialog lain menutupi" atau "elemen tidak ditemukan" perlu perbaikan selector atau penanganan dialog di skrip, bukan perubahan spek.
- Daftar ini belum berisi keputusan dari modul lain. Setiap modul punya dokumen sendiri di folder ini.
