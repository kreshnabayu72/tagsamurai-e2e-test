---
id: TC-FA-SU-E2E-248-tab-system-log-setup-column-bagian-1
title: "Tab System Log: Setup Column (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-754
coverage:
  web: automated
---

# Tab System Log: Setup Column (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan System Log (#28). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Tab System Log Budi Santoso (Pre-setup #28, 7 baris; urutan default Date descending; kolom Name berisi target perubahan). Alias baris yang dipakai langkah (Action | Name | Field):
  - S-1: `Resend Activation Email` | `Hana Kusuma` | `Activation Email`
  - S-2: `Auto-Revert` | `Oscar Pranata` | `Group Manager — IT Infrastructure`
  - S-3: `Edit` | `Oscar Pranata` | `Manage group — IT Infrastructure — Update`
  - S-4: `Assign` | `Lina Marlina` | `Access Level`
  - S-5: `Assign` | `Eka Wulandari` | `Manage group — Finance & Accounting`
  - S-6: `Assign` | `Eka Wulandari` | `Manage accounting`
  - S-7: `Activate` | `Eka Wulandari` | `Status`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed System Log #28 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface System Log dan tidak menambah entri pada Budi Santoso.
- Tabel "Kolom Setup Column Hideable" (parameter langkah berulang): Date, Action, Object, Name, Field, Old Value, New Value.
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.

## Test Steps

### TC-FA-SU-754: Ceklis dan unceklis Setup Column kelas Hideable

1. Buka Detail pengguna Budi Santoso lalu klik tab System Log
2. Buka Setup Column (klik header kolom Column Visibility (⋯), lalu `Setup Column...`)
3. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" selain New Value (langkah 4 sampai 5):
4. Hilangkan centang kolom tersebut pada daftar Setup Column
5. Verifikasi perubahan tampil di Live Preview (kolom tersebut tidak tampil)
6. Hover checkbox kolom New Value yang disabled
7. Verifikasi checkbox kolom New Value disabled dengan tooltip `At least one column must remain visible.` karena menjadi satu-satunya kolom visible
8. Klik `[Save]`
9. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" selain New Value (langkah 10):
10. Verifikasi kolom tersebut tidak tampil di tabel
11. Klik F5
12. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" selain New Value (langkah 13):
13. Verifikasi kolom tersebut tetap tidak tampil di tabel setelah refresh (F5)
14. Buka Setup Column, centang kembali seluruh kolom selain New Value, lalu hilangkan centang kolom New Value
15. Verifikasi perubahan kolom New Value tampil di Live Preview
16. Klik `[Save]`
17. Verifikasi kolom New Value tidak tampil di tabel
18. Klik F5
19. Verifikasi kolom New Value tetap tidak tampil di tabel setelah refresh (F5)
20. Hapus preferensi kolom tabel di browser lalu muat ulang halaman (kemampuan disediakan tim FE)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung tambahan (S-03): langkah 6 (Hover checkbox kolom New Value yang disabled) hanya memunculkan tooltip sebelum `Verifikasi` tooltip pada langkah 7 (bagian 8b butir 5); tidak ada asersi.
- Langkah berulang per kolom (idiom bagian 8b butir 7): langkah 4 sampai 5 dijalankan 6 kali, satu iterasi per kolom di tabel Prerequisites; langkah 10 dijalankan 6 kali, satu iterasi per kolom di tabel Prerequisites; langkah 13 dijalankan 6 kali, satu iterasi per kolom di tabel Prerequisites.
- Spec ini berjumlah 40 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #28 yang disediakan ulang di hook `before` dan `after` (S-14). Aksi spec lain terhadap Budi Santoso menambah entri System Log, sehingga penyediaan ulang seed menjadi syarat asersi urutan dan jumlah baris. (2) TC tidak menyebut cara menguji kolom yang menjadi satu-satunya kolom visible; spec menguji enam kolom pertama bersamaan lalu kolom terakhir terpisah setelah kolom lain dicentang kembali. Post Condition preferensi kolom tersimpan per perangkat tidak punya langkah observasi dan tidak diasersi.
