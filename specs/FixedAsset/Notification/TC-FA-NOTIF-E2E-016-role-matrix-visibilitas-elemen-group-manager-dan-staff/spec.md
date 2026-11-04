---
id: TC-FA-NOTIF-E2E-016-role-matrix-visibilitas-elemen-group-manager-dan-staff
title: "Role Matrix: Visibilitas Elemen Notifikasi Group Manager dan Staff"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-61
  - TC-FA-NOTIF-62
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Notifikasi Group Manager dan Staff

## Prerequisites

- Mode: FE+BE.
- Spec Role Matrix (bagian 3a konvensi): langkah visibilitas identik untuk kedua role, hanya akun login yang berbeda. Role yang diuji, urutan baris = urutan iterasi:

  | TC | Role | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|---|
  | TC-FA-NOTIF-61 | Group Manager (Gedung A) | #3 | `groupManagerFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` | `Fixture.fixedAssetNotification.groupManager` |
  | TC-FA-NOTIF-62 | Staff (Transaction Role Disposal, Gedung A) | #9 | `staffDisposal_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_STAFFDSP_PASSWORD` | `Fixture.fixedAssetNotification.staffDisposal` |

- Login akun aktor pertama (Group Manager, Pre-setup #3) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup (tetap di environment): seed notifikasi Pre-setup #17 untuk kedua akun: N-01 `Waiting for your approval` BRW-2026-0341 (2 Assets) Unread actionable; N-02 `Please confirm your borrowed asset` Kamera DSLR (AST-2024-0141) Unread actionable; N-03 `Asset has been repaired` Unread view-only; N-04 `Asset has been found` Laptop - 1 (AST-2024-0067) Unread view-only; N-05 `Your Total Control access was removed` Unread view-only; N-06 `Your request has been rejected` BRW-2026-0341 Read view-only; N-07 `New audit task started` Read actionable. Group Manager Gedung A memegang struktur Gedung A > Lantai 1 > Ruang 101 (Pre-setup #3 dan #24). Spec hanya membaca seed ini.
- Fixture BE pemulih seed notifikasi Pre-setup #17 sampai #24 dijalankan di hook `before` dan `after` (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`); efeknya mengembalikan seed kedua akun ke N-01 sampai N-07.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk kedua akun: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_GM_PASSWORD` dan `FA_STAFFDSP_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-61 dan TC-FA-NOTIF-62: Visibilitas elemen notifikasi per role

1. Untuk setiap baris tabel Role yang diuji (langkah 1 sampai 8): logout, lalu login sebagai role pada baris tabel dengan env var password baris itu, lalu buka Fixed Asset > Dashboard
2. Klik Bell icon
3. Verifikasi Bell icon dan Dropdown Panel tampil (Show)
4. Verifikasi tombol `[Detail]` pada item N-01 (actionable Unread; untuk Group Manager item dalam scope group Gedung A) tampil (Show)
5. Verifikasi tombol `[Mark as Read]` pada item N-03 (view-only Unread) tampil (Show)
6. Klik `[Show All]`
7. Verifikasi Notification Center dengan Tab All dan Tab Unread tampil (Show)
8. Verifikasi tidak ada elemen Hidden atau Disabled berbasis role: Bell icon, `[Detail]` pada item N-01, `[Mark as Read]` pada item N-03, Tab All, dan Tab Unread tampil dan aktif

## Notes

- Pengulangan (bagian 8b butir 7): langkah 1 sampai 8 diulang untuk tiap baris tabel Role yang diuji (dua baris, 16 langkah setelah ekspansi). Langkah 1 pada iterasi pertama melakukan logout dan login ulang akun yang sama dengan akun hook `before` supaya isi langkah identik untuk kedua role (S-07).
- Langkah penghubung (S-03): langkah 1 (ganti akun dan buka Fixed Asset > Dashboard); langkah 6 membuka Notification Center lewat `[Show All]` karena TC tidak menyebut jalur lain.
- Klausa "dalam scope group" pada langkah 4 hanya berasal dari Expected c TC-FA-NOTIF-61; TC-FA-NOTIF-62 menulis `[Detail]` pada item actionable Unread tanpa klausa itu. Langkah TC "Amati item N-01 dan N-03" tidak ditulis terpisah; pengamatannya dicakup `Verifikasi` langkah 4 dan 5. Expected e ditulis sebagai satu `Verifikasi` rangkuman atas elemen a sampai d (S-03).
- Temuan untuk QA:
  - Kolom Post Condition kedua TC kosong (`-`); tidak ada yang diasersi.
  - Judul TC-FA-NOTIF-62 menyebut "user lain pemegang Transaction Role Staff" tanpa nomor Pre-setup; spec memakai akun Pre-setup #9 (Transaction Role Staff Disposal) menurut tabel Pre-setup.
