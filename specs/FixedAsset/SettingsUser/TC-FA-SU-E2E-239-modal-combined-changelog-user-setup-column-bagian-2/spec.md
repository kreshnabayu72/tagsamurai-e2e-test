---
id: TC-FA-SU-E2E-239-modal-combined-changelog-user-setup-column-bagian-2
title: "Modal Combined Changelog: User: Setup Column (Bagian 2)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-725
  - TC-FA-SU-727
coverage:
  web: automated
---

# Modal Combined Changelog: User: Setup Column (Bagian 2)

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
- Tabel "Urutan Drag Setup Column" (parameter langkah berulang; dijalankan berurutan dari baris pertama, tiap baris drag satu posisi tanpa `[Save]` di antaranya sehingga efeknya kumulatif; posisi 1 = paling atas pada daftar Setup Column dan paling kiri pada tabel; posisi akhir dihitung dari urutan semula pada tabel "Kolom Setup Column Hideable"): (1) Action ke atas, posisi akhir 1; (2) Date ke bawah, posisi akhir 2; (3) User Name ke bawah, posisi akhir 4; (4) Field ke bawah, posisi akhir 6; (5) Old Value ke atas, posisi akhir 3; (6) New Value ke bawah, posisi akhir 7; (7) Modified By ke atas, posisi akhir 5.
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.

## Test Steps

### TC-FA-SU-725: Geser (drag reorder) Setup Column kelas Hideable

1. Klik icon Changelog di Table Tools halaman User List
2. Buka Setup Column (klik header kolom Column Visibility (⋯), lalu `Setup Column...`)
3. Untuk setiap baris pada tabel "Urutan Drag Setup Column" secara berurutan (langkah 4 sampai 5):
4. Drag kolom pada baris tersebut satu posisi ke arah (atas atau bawah) yang tertulis pada tabel
5. Verifikasi urutan Live Preview berubah
6. Klik `[Save]`
7. Untuk setiap baris pada tabel "Urutan Drag Setup Column" (langkah 8):
8. Verifikasi posisi kolom tersebut pada tabel berubah (menempati posisi akhir pada tabel)
9. Klik F5
10. Untuk setiap baris pada tabel "Urutan Drag Setup Column" (langkah 11):
11. Verifikasi posisi kolom tersebut pada tabel tetap berubah (menempati posisi akhir pada tabel) setelah refresh (F5)
12. Hapus preferensi kolom tabel di browser lalu muat ulang halaman (kemampuan disediakan tim FE)

### TC-FA-SU-727: Reset to Default, Discard (✕ atau Esc), dan independensi cache Setup Column

13. Klik icon Changelog di Table Tools halaman User List
14. Buka Setup Column (klik header kolom Column Visibility (⋯), lalu `Setup Column...`), sembunyikan satu kolom dan pin satu kolom
15. Klik `[Reset to Default]`
16. Verifikasi visibility, urutan, dan pin kembali ke default modul pada preview
17. Klik `[Save]`
18. Verifikasi konfigurasi default menjadi permanen setelah `[Save]`
19. Buka Setup Column, sembunyikan satu kolom, lalu tutup lewat ✕
20. Verifikasi perubahan preview dibuang dan tabel memakai konfigurasi tersimpan terakhir
21. Buka Setup Column, sembunyikan satu kolom, lalu tekan Esc
22. Verifikasi perubahan preview dibuang dan tabel memakai konfigurasi tersimpan terakhir
23. Buka Setup Column, sembunyikan satu kolom, klik `[Save]`, lalu tutup modal dan buka Setup Column tabel User List
24. Verifikasi konfigurasi tabel lain tidak terpengaruh perubahan tabel ini (cache per tabel)
25. Hapus preferensi kolom tabel di browser lalu muat ulang halaman (kemampuan disediakan tim FE)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah berulang per kolom (idiom bagian 8b butir 7): langkah 4 sampai 5 dijalankan 7 kali, satu iterasi per kolom di tabel Prerequisites; langkah 8 dijalankan 7 kali, satu iterasi per kolom di tabel Prerequisites; langkah 11 dijalankan 7 kali, satu iterasi per kolom di tabel Prerequisites.
- TC-FA-SU-724 ada di spec 238 dan TC-FA-SU-726 ada di spec 252.
- Spec ini berjumlah 49 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #27 yang disediakan ulang di hook `before` dan `after` (S-14). Modal Combined Changelog memuat riwayat seluruh pengguna Client, sehingga entri dari spec lain (Activate, Deactivate, Resend, Edit Home Group) menambah baris di surface ini; TC tidak menyatakan cara menjaga isi keenam baris seed selain penyediaan ulang seed. (2) TC-FA-SU-725 tidak menyebut arah drag; spec menulis "satu posisi" mengikuti TC dan menetapkan sendiri urutan, arah, dan posisi akhir tiap kolom pada tabel "Urutan Drag Setup Column" di Prerequisites, karena drag berurutan tanpa `[Save]` bersifat kumulatif sehingga arah yang tidak ditentukan membuat posisi akhir tidak deterministik; arah dan posisi akhir itu pilihan spec, bukan ketentuan TC. Post Condition preferensi kolom tersimpan per perangkat tidak punya langkah observasi dan tidak diasersi. (3) TC-FA-SU-727 langkah 6 menyebut `tabel lain yang punya Setup Column` tanpa nama; spec memakai tabel User List. (4) Langkah `[Save]` pada langkah "Buka Setup Column, sembunyikan satu kolom, klik `[Save]`, lalu tutup modal dan buka Setup Column tabel User List" ditambahkan spec tanpa dasar TC: TC-FA-SU-727 langkah 4 dan 5 hanya menutup lewat ✕ atau Esc, dan langkah 6 membandingkan tabel lain tanpa menyebut Save. Save dipilih agar perubahan tersimpan di tabel ini sebelum dibandingkan dengan User List (Expected c); pemilik TC perlu mengonfirmasi atau menyatakan cara lain.
