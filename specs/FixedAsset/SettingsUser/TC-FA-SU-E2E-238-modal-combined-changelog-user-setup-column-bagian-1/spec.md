---
id: TC-FA-SU-E2E-238-modal-combined-changelog-user-setup-column-bagian-1
title: "Modal Combined Changelog: User: Setup Column (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-724
coverage:
  web: automated
---

# Modal Combined Changelog: User: Setup Column (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Changelog (#27). Modal Combined Changelog dibuka dari icon Changelog di Table Tools halaman User List dan memuat riwayat seluruh pengguna Client `FaUserMain`. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Modal Combined Changelog (Pre-setup #27, 6 baris; urutan default Date descending). Alias baris yang dipakai langkah (Action | User Name | Field; Modified By dalam format `[First Name] [Last Initial]`):
  - C-1: `Resend Activation Email` | `Hana Kusuma` | `Activation Email`; Modified By `Ahmad D`
  - C-2: `Deactivate` | `Doni Prasetyo` | `Status`; Modified By `Budi S`
  - C-3: `Edit Home Group` | `Budi Santoso` | `Home Group`; Modified By `Lina M`
  - C-4: `Edit` | `Gita Permata` | `Manage group — Finance & Accounting — Update`; Modified By `Ahmad D`
  - C-5: `Assign` | `Budi Santoso` | `Manage accounting`; Modified By `Ahmad D`
  - C-6: `Activate` | `Eka Wulandari` | `Status`; Modified By `Ahmad D`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed Changelog #27 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface Combined Changelog dan tidak menambah entri.
- Tabel "Kolom Setup Column Hideable" (parameter langkah berulang): Date, Action, User Name, Field, Old Value, New Value, Modified By.
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.

## Test Steps

### TC-FA-SU-724: Ceklis dan unceklis Setup Column kelas Hideable

1. Klik icon Changelog di Table Tools halaman User List
2. Buka Setup Column (klik header kolom Column Visibility (⋯), lalu `Setup Column...`)
3. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" selain Modified By (langkah 4 sampai 5):
4. Hilangkan centang kolom tersebut pada daftar Setup Column
5. Verifikasi perubahan tampil di Live Preview (kolom tersebut tidak tampil)
6. Hover checkbox kolom Modified By yang disabled
7. Verifikasi checkbox kolom Modified By disabled dengan tooltip `At least one column must remain visible.` karena menjadi satu-satunya kolom visible
8. Klik `[Save]`
9. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" selain Modified By (langkah 10):
10. Verifikasi kolom tersebut tidak tampil di tabel
11. Klik F5
12. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" selain Modified By (langkah 13):
13. Verifikasi kolom tersebut tetap tidak tampil di tabel setelah refresh (F5)
14. Buka Setup Column, centang kembali seluruh kolom selain Modified By, lalu hilangkan centang kolom Modified By
15. Verifikasi perubahan kolom Modified By tampil di Live Preview
16. Klik `[Save]`
17. Verifikasi kolom Modified By tidak tampil di tabel
18. Klik F5
19. Verifikasi kolom Modified By tetap tidak tampil di tabel setelah refresh (F5)
20. Hapus preferensi kolom tabel di browser lalu muat ulang halaman (kemampuan disediakan tim FE)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung tambahan (S-03): langkah 6 (Hover checkbox kolom Modified By yang disabled) hanya memunculkan tooltip sebelum `Verifikasi` tooltip pada langkah 7 (bagian 8b butir 5); tidak ada asersi.
- Langkah berulang per kolom (idiom bagian 8b butir 7): langkah 4 sampai 5 dijalankan 6 kali, satu iterasi per kolom di tabel Prerequisites; langkah 10 dijalankan 6 kali, satu iterasi per kolom di tabel Prerequisites; langkah 13 dijalankan 6 kali, satu iterasi per kolom di tabel Prerequisites.
- Spec ini berjumlah 40 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #27 yang disediakan ulang di hook `before` dan `after` (S-14). Modal Combined Changelog memuat riwayat seluruh pengguna Client, sehingga entri dari spec lain (Activate, Deactivate, Resend, Edit Home Group) menambah baris di surface ini; TC tidak menyatakan cara menjaga isi keenam baris seed selain penyediaan ulang seed. (2) TC tidak menyebut cara menguji kolom yang menjadi satu-satunya kolom visible; spec menguji enam kolom pertama bersamaan lalu kolom terakhir terpisah setelah kolom lain dicentang kembali. Post Condition preferensi kolom tersimpan per perangkat tidak punya langkah observasi dan tidak diasersi.
