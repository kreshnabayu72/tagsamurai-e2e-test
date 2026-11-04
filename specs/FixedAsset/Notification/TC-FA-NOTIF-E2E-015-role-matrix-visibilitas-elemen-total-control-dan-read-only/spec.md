---
id: TC-FA-NOTIF-E2E-015-role-matrix-visibilitas-elemen-total-control-dan-read-only
title: "Role Matrix: Visibilitas Elemen Notifikasi Total Control dan Read Only"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-59
  - TC-FA-NOTIF-60
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Notifikasi Total Control dan Read Only

## Prerequisites

- Mode: FE+BE.
- Spec Role Matrix (bagian 3a konvensi): langkah visibilitas identik untuk semua role, hanya akun login yang berbeda. Role yang diuji, urutan baris = urutan iterasi:

  | TC | Role | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|---|
  | TC-FA-NOTIF-59 | Total Control | #1 | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` | `Fixture.fixedAssetNotification.totalControl` |
  | TC-FA-NOTIF-60 | Read Only | #2 | `readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` | `Fixture.fixedAssetNotification.readOnly` |

- Login akun aktor pertama (Total Control, Pre-setup #1) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup (tetap di environment): seed notifikasi Pre-setup #17 untuk kedua akun: N-01 `Waiting for your approval` BRW-2026-0341 (2 Assets) Unread actionable; N-02 `Please confirm your borrowed asset` Kamera DSLR (AST-2024-0141) Unread actionable; N-03 `Asset has been repaired` Unread view-only; N-04 `Asset has been found` Laptop - 1 (AST-2024-0067) Unread view-only; N-05 `Your Total Control access was removed` Unread view-only; N-06 `Your request has been rejected` BRW-2026-0341 Read view-only; N-07 `New audit task started` Read actionable. Spec hanya membaca seed ini.
- Fixture BE pemulih seed notifikasi Pre-setup #17 sampai #24 dijalankan di hook `before` dan `after` (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`); efeknya mengembalikan seed kedua akun ke N-01 sampai N-07.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk kedua akun: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_TC_PASSWORD` dan `FA_RO_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-59 dan TC-FA-NOTIF-60: Visibilitas elemen notifikasi per role

1. Untuk setiap baris tabel Role yang diuji (langkah 1 sampai 8): logout, lalu login sebagai role pada baris tabel dengan env var password baris itu, lalu buka Fixed Asset > Dashboard
2. Klik Bell icon
3. Verifikasi Bell icon dan Dropdown Panel tampil (Show)
4. Verifikasi tombol `[Detail]` pada item N-01 (actionable Unread) tampil (Show)
5. Verifikasi tombol `[Mark as Read]` pada item N-03 (view-only Unread) tampil (Show)
6. Klik `[Show All]`
7. Verifikasi Notification Center dengan Tab All dan Tab Unread tampil (Show)
8. Verifikasi tidak ada elemen Hidden atau Disabled berbasis role: Bell icon, `[Detail]` pada item N-01, `[Mark as Read]` pada item N-03, Tab All, dan Tab Unread tampil dan aktif

## Notes

- Pengulangan (bagian 8b butir 7): langkah 1 sampai 8 diulang untuk tiap baris tabel Role yang diuji (dua baris, 16 langkah setelah ekspansi). Langkah 1 pada iterasi pertama melakukan logout dan login ulang akun yang sama dengan akun hook `before` supaya isi langkah identik untuk semua role (S-07).
- Langkah penghubung (S-03): langkah 1 (ganti akun dan buka Fixed Asset > Dashboard); langkah 6 membuka Notification Center lewat `[Show All]` karena TC tidak menyebut jalur lain.
- Langkah TC "Amati item N-01 dan N-03" tidak ditulis sebagai langkah terpisah; pengamatannya dicakup `Verifikasi` langkah 4 dan 5. Expected e ("Tidak ada elemen Hidden atau Disabled berbasis role") ditulis sebagai satu `Verifikasi` rangkuman atas elemen a sampai d (S-03, kesimpulan yang tidak teramati terpisah).
- Temuan untuk QA:
  - Kolom Post Condition kedua TC kosong (`-`); tidak ada yang diasersi.
  - Tabel Pre-setup tidak menulis seed notifikasi per akun untuk Read Only (Pre-setup #2); TC mensyaratkan N-01 sampai N-07 tersedia untuk akun ini, sehingga spec mengandalkan fixture BE pemulih seed untuk kedua akun.
