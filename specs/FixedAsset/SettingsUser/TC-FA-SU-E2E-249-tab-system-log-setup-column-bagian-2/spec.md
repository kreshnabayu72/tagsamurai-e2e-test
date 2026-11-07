---
id: TC-FA-SU-E2E-249-tab-system-log-setup-column-bagian-2
title: "Tab System Log: Setup Column (Bagian 2)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-755
  - TC-FA-SU-757
coverage:
  web: automated
---

# Tab System Log: Setup Column (Bagian 2)

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
- Tabel "Urutan Drag Setup Column" (parameter langkah berulang; dijalankan berurutan dari baris pertama, tiap baris drag satu posisi tanpa `[Save]` di antaranya sehingga efeknya kumulatif; posisi 1 = paling atas pada daftar Setup Column dan paling kiri pada tabel; posisi akhir dihitung dari urutan semula pada tabel "Kolom Setup Column Hideable"): (1) Action ke atas, posisi akhir 1; (2) Date ke bawah, posisi akhir 2; (3) Object ke bawah, posisi akhir 4; (4) Name ke bawah, posisi akhir 6; (5) Field ke atas, posisi akhir 3; (6) Old Value ke bawah, posisi akhir 7; (7) New Value ke atas, posisi akhir 5.
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.

## Test Steps

### TC-FA-SU-755: Geser (drag reorder) Setup Column kelas Hideable

1. Ketik Search `Budi Santoso`, tekan Enter
2. Buka Detail pengguna Budi Santoso lalu klik tab System Log
3. Buka Setup Column (klik header kolom Column Visibility (⋯), lalu `Setup Column...`)
4. Untuk setiap baris pada tabel "Urutan Drag Setup Column" secara berurutan (langkah 5 sampai 6):
5. Drag kolom pada baris tersebut satu posisi ke arah (atas atau bawah) yang tertulis pada tabel
6. Verifikasi urutan Live Preview berubah
7. Klik `[Save]`
8. Untuk setiap baris pada tabel "Urutan Drag Setup Column" (langkah 9):
9. Verifikasi posisi kolom tersebut pada tabel berubah (menempati posisi akhir pada tabel)
10. Klik F5
11. Untuk setiap baris pada tabel "Urutan Drag Setup Column" (langkah 12):
12. Verifikasi posisi kolom tersebut pada tabel tetap berubah (menempati posisi akhir pada tabel) setelah refresh (F5)
13. Hapus preferensi kolom tabel di browser lalu muat ulang halaman (kemampuan disediakan tim FE)

### TC-FA-SU-757: Reset to Default, Discard (✕ atau Esc), dan independensi cache Setup Column

14. Kembali ke User List, ganti isi kotak search dengan `Budi Santoso`, tekan Enter
15. Buka Detail pengguna Budi Santoso lalu klik tab System Log
16. Buka Setup Column (klik header kolom Column Visibility (⋯), lalu `Setup Column...`), sembunyikan satu kolom dan pin satu kolom
17. Klik `[Reset to Default]`
18. Verifikasi visibility, urutan, dan pin kembali ke default modul pada preview
19. Klik `[Save]`
20. Verifikasi konfigurasi default menjadi permanen setelah `[Save]`
21. Buka Setup Column, sembunyikan satu kolom, lalu tutup lewat ✕
22. Verifikasi perubahan preview dibuang dan tabel memakai konfigurasi tersimpan terakhir
23. Buka Setup Column, sembunyikan satu kolom, lalu tekan Esc
24. Verifikasi perubahan preview dibuang dan tabel memakai konfigurasi tersimpan terakhir
25. Buka Setup Column, sembunyikan satu kolom, klik `[Save]`, lalu buka halaman User List dan buka Setup Column tabel User List
26. Verifikasi konfigurasi tabel lain tidak terpengaruh perubahan tabel ini (cache per tabel)
27. Hapus preferensi kolom tabel di browser lalu muat ulang halaman (kemampuan disediakan tim FE)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (Ketik Search `Budi Santoso` di User List) dan langkah 14 (ganti isi kotak search dengan `Budi Santoso`; kotak Search mempertahankan nilainya sesudah muat ulang, butir 8b.9) untuk menemukan baris target sebelum membuka Detail, R-16, butir 8b.13; User List memuat 25 pengguna pada 3 halaman sehingga posisi baris tidak diandalkan.
- Langkah berulang per kolom (idiom bagian 8b butir 7): langkah 5 sampai 6 dijalankan 7 kali, satu iterasi per kolom di tabel Prerequisites; langkah 9 dijalankan 7 kali, satu iterasi per kolom di tabel Prerequisites; langkah 12 dijalankan 7 kali, satu iterasi per kolom di tabel Prerequisites.
- TC-FA-SU-754 ada di spec 248 dan TC-FA-SU-756 ada di spec 253.
- Spec ini berjumlah 51 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #28 yang disediakan ulang di hook `before` dan `after` (S-14). Aksi spec lain terhadap Budi Santoso menambah entri System Log, sehingga penyediaan ulang seed menjadi syarat asersi urutan dan jumlah baris. (2) TC-FA-SU-755 tidak menyebut arah drag; spec menulis "satu posisi" mengikuti TC dan menetapkan sendiri urutan, arah, dan posisi akhir tiap kolom pada tabel "Urutan Drag Setup Column" di Prerequisites, karena drag berurutan tanpa `[Save]` bersifat kumulatif sehingga arah yang tidak ditentukan membuat posisi akhir tidak deterministik; arah dan posisi akhir itu pilihan spec, bukan ketentuan TC. Post Condition preferensi kolom tersimpan per perangkat tidak punya langkah observasi dan tidak diasersi. (3) TC-FA-SU-757 langkah 6 menyebut `tabel lain yang punya Setup Column` tanpa nama; spec memakai tabel User List. (4) Langkah `[Save]` pada langkah 25 ("Buka Setup Column, sembunyikan satu kolom, klik `[Save]`, lalu buka halaman User List") ditambahkan spec tanpa dasar TC-FA-SU-757: TC langkah 4 dan 5 hanya menutup lewat ✕ atau Esc, dan langkah 6 membandingkan tabel lain tanpa menyebut Save. Save dipilih agar perubahan tersimpan di tabel ini sebelum dibandingkan dengan User List (Expected c); mohon konfirmasi atau hapus.
