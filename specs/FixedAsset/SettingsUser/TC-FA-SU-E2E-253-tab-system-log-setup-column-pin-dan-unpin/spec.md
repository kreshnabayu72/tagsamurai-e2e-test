---
id: TC-FA-SU-E2E-253-tab-system-log-setup-column-pin-dan-unpin
title: "Tab System Log: Setup Column Pin dan Unpin"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-756
coverage:
  web: automated
---

# Tab System Log: Setup Column Pin dan Unpin

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
- Viewport browser dipersempit agar tabel dapat di-scroll horizontal (dipakai langkah 5, 7, dan 9); dipulihkan di hook `after`.
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.

## Test Steps

### TC-FA-SU-756: Pin dan unpin Setup Column kelas Hideable

1. Ketik Search `Budi Santoso`, tekan Enter
2. Buka Detail pengguna Budi Santoso lalu klik tab System Log
3. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" (langkah 4 sampai 10):
4. Buka Setup Column lalu klik icon Pin pada kolom tersebut
5. Klik `[Save]`, lalu scroll tabel secara horizontal
6. Verifikasi kolom tersebut membeku di kiri saat tabel di-scroll horizontal
7. Klik F5, lalu scroll tabel secara horizontal
8. Verifikasi kolom tersebut tetap membeku di kiri setelah refresh (F5)
9. Buka Setup Column lalu unpin kolom tersebut, klik `[Save]`, lalu scroll tabel secara horizontal
10. Verifikasi kolom tersebut terlepas (tidak lagi membeku) saat tabel di-scroll horizontal
11. Buka Setup Column lalu klik icon Pin pada tiga kolom pertama
12. Hover icon Pin pada salah satu kolom lain
13. Verifikasi icon Pin kolom lain disabled dengan tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
14. Hapus preferensi kolom tabel di browser lalu muat ulang halaman (kemampuan disediakan tim FE)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (Ketik Search `Budi Santoso` di User List untuk menemukan baris target sebelum membuka Detail, R-16, butir 8b.13); User List memuat 25 pengguna pada 3 halaman sehingga posisi baris tidak diandalkan.
- Langkah penghubung tambahan: Hover icon Pin pada kolom lain (langkah 12) sebelum `Verifikasi` tooltip, supaya tooltip muncul (bukan `Verifikasi`).
- Langkah berulang per kolom (idiom bagian 8b butir 7): langkah 4 sampai 10 dijalankan 7 kali, satu iterasi per kolom di tabel Prerequisites.
- TC-FA-SU-754 ada di spec 248 dan TC-FA-SU-755 serta TC-FA-SU-757 ada di spec 249.
- Spec ini berjumlah 56 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #28 yang disediakan ulang di hook `before` dan `after` (S-14). Aksi spec lain terhadap Budi Santoso menambah entri System Log, sehingga penyediaan ulang seed menjadi syarat asersi urutan dan jumlah baris. (2) Post Condition preferensi kolom tersimpan per perangkat tidak punya langkah observasi dan tidak diasersi. TC-FA-SU-756 langkah 3 menyebut pin pada daftar kolom sekaligus, sedangkan Expected h membatasi tiga kolom; spec mem-pin satu kolom per iterasi lalu menguji batas tiga kolom.
