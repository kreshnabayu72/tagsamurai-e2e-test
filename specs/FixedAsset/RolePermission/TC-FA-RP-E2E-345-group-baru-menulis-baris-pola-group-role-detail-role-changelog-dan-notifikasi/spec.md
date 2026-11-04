---
id: TC-FA-RP-E2E-345-group-baru-menulis-baris-pola-group-role-detail-role-changelog-dan-notifikasi
title: "Group baru (Subgroup, level 1, dan hasil Import) menulis baris pola Group Role dengan log Assign biasa dan tanpa notifikasi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1174
coverage:
  web: automated
---

# Group baru (Subgroup, level 1, dan hasil Import) menulis baris pola Group Role dengan log Assign biasa dan tanpa notifikasi

## Prerequisites

- Mode: FE+BE.
- Akun:

| Urutan | Akun | Pre-setup | Email | Env password |
|---|---|---|---|---|
| 1 (hook `before`) | Total Control, Siti Rahmawati | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| 2 | Total Control kedua, Rina Wulandari | #3 | `totalControlSecond_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC2_PASSWORD` |

- Login akun urutan 1 di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #18 (pohon Group; `IT Infrastructure` menjadi induk Subgroup), #3 (Rina Wulandari), #12 (Maya Anggraeni), #24 (`Company Changelog`, log 25 entri campuran; dipakai sebagai latar log, tidak diasersi).
- Baris pola yang diharapkan pada ketiga Group baru (Group Role `Manage files`): Admin Utama (Default User), Siti Rahmawati, dan Rina Wulandari (Total Control) dengan Read dan Delete aktif; Dewi Anggraini dan Maya Anggraeni (Read Only) dengan Read saja.
- Data Dinamis (bersuffix `{runId}` dan nomor spec 345): Subgroup `Pola Create {runId}-345` di bawah `IT Infrastructure`, Group level 1 `Pola Root {runId}-345`, Group hasil Import `Pola Import {runId}-345`. Berkas Import `Fixture.fixedAssetRolePermission.berkasImportGroupPola` (belum ada; disediakan tim FE) memuat satu Group level 1 bernama `Pola Import {runId}-345`. Pembuatan ketiga Group (langkah 3 sampai 6) membentuk precondition d TC dan tidak diasersi di spec ini.
- Kemampuan teknis: membaca jumlah notifikasi in-app Rina Wulandari sebagai baseline (disediakan tim FE/BE, tanpa endpoint karangan); jendela absence notifikasi "Tunggu 5 detik tanpa memuat ulang halaman" adalah pilihan spec (bukan nilai TC atau PRD).
- Pemulihan (hook `after`, tidak berasumsi pembuatan berhasil penuh): ketiga Group dinamis dihapus lewat sesi API Total Control (kemampuan disediakan tim FE/BE). Tabel Data Uji Dinamis TC menulis ketiga Group "tetap ada sampai akhir sesi"; spec ini menghapusnya di hook `after` supaya tidak menumpang run lain (S-06).
- Env var yang dipakai: `FA_TC_PASSWORD`, `FA_TC2_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

Node yang ditelusuri pada langkah 9 sampai 11:

| Node pola |
|---|
| `Pola Create {runId}-345` |
| `Pola Root {runId}-345` |
| `Pola Import {runId}-345` |

## Test Steps

### Persiapan Group baru (precondition TC, tidak diasersi)

1. Catat jumlah notifikasi in-app Rina Wulandari sebagai baseline lewat kemampuan baca
2. Buka Fixed Asset > Settings > Groups
3. Buat Subgroup `Pola Create {runId}-345` di bawah `IT Infrastructure` lewat row action `Add Subgroup`
4. Buat Group level 1 `Pola Root {runId}-345`
5. Import Group `Pola Import {runId}-345` lewat Import di Settings > Groups dengan berkas Import `Fixture.fixedAssetRolePermission.berkasImportGroupPola`
6. Tunggu aksi selesai (ketiga Group tampil di pohon Group)

### TC-FA-RP-1174: Group baru menulis baris pola Group Role Default User, Total Control, dan Read Only dengan log Assign biasa dan tanpa notifikasi

7. Buka Fixed Asset > Settings > Role & Permission > System dan buka Detail Role Group Role `Manage files`
8. Untuk setiap baris tabel "Node pola": klik node pada Sidebar Group Tree (langkah 9 dan 10 diulang untuk node itu)
9. Verifikasi Admin Utama (Default User), Siti Rahmawati, dan Rina Wulandari tampil dengan Read dan Delete aktif (CRUD penuh sesuai kolom berlaku) pada node itu
10. Verifikasi Dewi Anggraini dan Maya Anggraeni tampil dengan Read saja pada node itu
11. Klik node `Pola Import {runId}-345`
12. Verifikasi tabel node `Pola Import {runId}-345` hanya memuat kelima baris pola dan tidak ada penugasan Standard (tanpa pewarisan)
13. Klik ikon Changelog di toolbar Detail Role
14. Verifikasi modal memuat entri Action `Assign` (bukan `Assign (via Total Control)`) per baris pola untuk node `Pola Import {runId}-345`
15. Verifikasi entri tersebut memuat Old Value `—` dan New Value `Assigned`
16. Tutup modal Changelog
17. Ganti akun: logout, lalu login sebagai Total Control kedua Rina Wulandari
18. Klik Bell icon
19. Verifikasi panel notifikasi tampil
20. Tunggu 5 detik tanpa memuat ulang halaman
21. Verifikasi jumlah notifikasi Rina Wulandari sama dengan baseline langkah 1 (tidak ada notifikasi untuk pembuatan baris pola)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 21 langkah.
- Langkah penghubung (S-03): langkah 1 (baseline notifikasi, S-12), langkah 2 sampai 6 (pembentuk precondition d TC, tanpa `Verifikasi`), langkah 7, 8, 11, 16, 17, dan 18 (navigasi, penelusuran node, ganti akun), langkah 20 (jendela absence notifikasi, bagian 6). Tanpa Search pada tabel Detail Role: tiap node memuat paling banyak enam baris, dalam satu halaman. Langkah 19 adalah anchor positif tambahan di luar TC (8b butir 2 dan 11) untuk asersi absence langkah 21.
- Pembagian TC lintas spec: TC-FA-RP-1157 dan 1158 (surface Transaction Role atas Group yang sama) ada di spec 330. Precondition d TC-FA-RP-1174 menyebut Group dari TC-FA-RP-1157 dan 1158; spec ini membuat Group sendiri (konvensi: spec tidak menumpang spec lain).
- Pembacaan entri Changelog langkah 14 dan 15 memakai nama Group bersuffix unik `{runId}-345` sehingga baseline entri nol (S-12); tidak ada asersi total entri.
- Temuan untuk QA:
  - TC-FA-RP-1174 tumpang tindih dengan TC-FA-RP-1157 dan 1158 (Group yang sama, surface berbeda). Ditempatkan terpisah per surface; mohon konfirmasi bahwa ini bukan duplikat yang seharusnya digabung di TC.
  - TC-FA-RP-1174 tidak menyebut client; spec memakai client default (Company Alpha). Precondition d merujuk Group dari TC-FA-RP-1157 yang berjalan di `Client Addon On`, sedangkan Detail Role `Manage files` tidak bergantung lisensi Addon.
  - TC-FA-RP-1174 mensyaratkan Pre-setup #24 (Company Changelog); TC tidak menyebut apakah #24 client terpisah atau seed log pada client default. Spec mengikuti spec 054 dan menganggap #24 latar log pada client default. `suite.md` belum menyebut Pre-setup #24 pada pernyataan Pre-setup bersama; pemulihan #24 dijamin tim FE/BE.
  - TC-FA-RP-1174 Expected b ("tidak ada penugasan Standard") tidak menyebut contoh nama; spec mengasersi tabel node `Pola Import {runId}-345` hanya memuat kelima baris pola (langkah 12).
  - TC-FA-RP-1174 Expected d ("tidak ada notifikasi") tidak punya anchor positif pengiriman notifikasi; spec memakai panel notifikasi yang terbuka dan selisih terhadap baseline.
  - Tabel Data Uji Dinamis TC memakai `{n}` untuk nama Group; spec memakai suffix `{runId}-345` (S-12).
  - TC-FA-RP-1174 mengasumsikan kolom "berlaku" CRUD penuh untuk Admin Utama, Siti Rahmawati, dan Rina Wulandari; spec hanya mengasersi Read dan Delete aktif sesuai Expected a.
