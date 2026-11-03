---
id: TC-FA-SU-E2E-294-tab-user-log-sub-tab-session-pin-dan-unpin-setup-column
title: "Tab User Log sub-tab Session: Pin dan Unpin Setup Column"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-885
coverage:
  web: automated
---

# Tab User Log sub-tab Session: Pin dan Unpin Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan User Log (#30). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Tab User Log sub-tab Session Budi Santoso (Pre-setup #30, 9 baris; urutan default Date descending). Label baris = `Date|Note` (kolom Activity bernilai `Session`, kolom Status bernilai `—`); alias dipakai langkah:
  - S-1: `16/07/26 08:12|Session started`
  - S-2: `15/07/26 20:30|Session ended`
  - S-3: `15/07/26 08:00|Session started`
  - S-4: `14/07/26 08:40|Session ended`, IP Address `192.0.2.40`, Device/Browser memuat `Safari`
  - S-5: `14/07/26 08:05|Session started`, IP Address `192.0.2.40`, Device/Browser memuat `Safari`
  - S-6: `13/07/26 17:05|Session ended`
  - S-7: `13/07/26 08:10|Session started`
  - S-8: `12/07/26 17:15|Session ended`
  - S-9: `12/07/26 08:02|Session started`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed User Log #30 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface User Log dan tidak menambah entri pada Budi Santoso.
- Tabel "Kolom Setup Column Hideable" (parameter langkah berulang): Date, Activity, Status, Note, IP Address, Device/Browser.
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.

## Test Steps

### TC-FA-SU-885: Pin dan unpin Setup Column kelas Hideable (default tampil)

1. Buka Detail pengguna Budi Santoso lalu klik tab User Log, sub-tab Session
2. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" (langkah 3 sampai 9):
3. Buka Setup Column lalu klik icon Pin pada kolom tersebut
4. Klik `[Save]`, lalu scroll tabel secara horizontal
5. Verifikasi kolom tersebut membeku di kiri saat tabel di-scroll horizontal
6. Klik F5
7. Verifikasi kolom tersebut tetap membeku di kiri setelah refresh (F5)
8. Buka Setup Column lalu unpin kolom tersebut, klik `[Save]`
9. Verifikasi kolom tersebut terlepas (tidak lagi membeku) saat tabel di-scroll horizontal
10. Buka Setup Column lalu klik icon Pin pada tiga kolom pertama
11. Hover icon Pin pada salah satu kolom lain
12. Verifikasi icon Pin kolom lain disabled dengan tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
13. Hapus preferensi kolom tabel di browser lalu muat ulang halaman (kemampuan disediakan tim FE)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung tambahan: Hover icon Pin pada kolom lain (langkah 11) sebelum `Verifikasi` tooltip, supaya tooltip muncul.
- Langkah berulang per kolom (idiom bagian 8b butir 7): langkah 3 sampai 9 dijalankan 6 kali, satu iterasi per kolom di tabel Prerequisites.
- Spec ini berjumlah 48 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- TC-FA-SU-883 dan TC-FA-SU-884 ada di spec 289; TC-FA-SU-886 ada di spec 290.
- Temuan untuk QA (S-15): (1) Post Condition preferensi kolom tersimpan per perangkat (atau kembali ke default) tidak punya langkah observasi di luar Expected dan tidak diasersi tambahan. Spec ini menyimpan konfigurasi Setup Column di browser; `suite.md` belum mencantumkan daftar spec yang menyimpan konfigurasi kolom (bagian 4 konvensi), sehingga perlu ditambahkan tim FE. (2) TC-FA-SU-885: Langkah Uji 3 meminta pin pada keenam kolom sekaligus, sedangkan Expected g membatasi tiga kolom; spec mem-pin satu kolom per iterasi lalu menguji batas tiga kolom. Post Condition preferensi kolom tersimpan per perangkat tidak punya langkah observasi dan tidak diasersi.
