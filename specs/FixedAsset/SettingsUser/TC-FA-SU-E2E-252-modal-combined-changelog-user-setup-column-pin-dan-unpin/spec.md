---
id: TC-FA-SU-E2E-252-modal-combined-changelog-user-setup-column-pin-dan-unpin
title: "Modal Combined Changelog: User: Setup Column Pin dan Unpin"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-726
coverage:
  web: automated
---

# Modal Combined Changelog: User: Setup Column Pin dan Unpin

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

### TC-FA-SU-726: Pin dan unpin Setup Column kelas Hideable

1. Klik icon Changelog di Table Tools halaman User List
2. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" (langkah 3 sampai 9):
3. Buka Setup Column lalu klik icon Pin pada kolom tersebut
4. Klik `[Save]`, lalu scroll tabel secara horizontal
5. Verifikasi kolom tersebut membeku di kiri saat tabel di-scroll horizontal
6. Klik F5
7. Verifikasi kolom tersebut tetap membeku di kiri setelah refresh (F5)
8. Buka Setup Column lalu unpin kolom tersebut, klik `[Save]`
9. Verifikasi kolom tersebut terlepas (tidak lagi membeku) saat tabel di-scroll horizontal
10. Buka Setup Column lalu klik icon Pin pada tiga kolom pertama
11. Hover icon Pin kolom lain yang disabled
12. Verifikasi icon Pin kolom lain disabled dengan tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
13. Hapus preferensi kolom tabel di browser lalu muat ulang halaman (kemampuan disediakan tim FE)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung tambahan (S-03): langkah 11 (Hover icon Pin kolom lain yang disabled) hanya memunculkan tooltip sebelum `Verifikasi` tooltip pada langkah 12 (bagian 8b butir 5); tidak ada asersi.
- Langkah berulang per kolom (idiom bagian 8b butir 7): langkah 3 sampai 9 dijalankan 7 kali, satu iterasi per kolom di tabel Prerequisites.
- TC-FA-SU-724 ada di spec 238 dan TC-FA-SU-725 serta TC-FA-SU-727 ada di spec 239.
- Spec ini berjumlah 55 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #27 yang disediakan ulang di hook `before` dan `after` (S-14). Modal Combined Changelog memuat riwayat seluruh pengguna Client, sehingga entri dari spec lain (Activate, Deactivate, Resend, Edit Home Group) menambah baris di surface ini; TC tidak menyatakan cara menjaga isi keenam baris seed selain penyediaan ulang seed. (2) Post Condition preferensi kolom tersimpan per perangkat tidak punya langkah observasi dan tidak diasersi. TC-FA-SU-726 langkah 3 menyebut pin pada daftar kolom sekaligus, sedangkan Expected h membatasi tiga kolom; spec mem-pin satu kolom per iterasi lalu menguji batas tiga kolom.
