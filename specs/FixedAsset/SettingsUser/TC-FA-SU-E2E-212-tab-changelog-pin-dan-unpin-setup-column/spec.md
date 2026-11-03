---
id: TC-FA-SU-E2E-212-tab-changelog-pin-dan-unpin-setup-column
title: "Tab Changelog: Pin dan Unpin Setup Column"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-598
coverage:
  web: automated
---

# Tab Changelog: Pin dan Unpin Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Changelog (#27). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Tab Changelog Budi Santoso (Pre-setup #27, 7 baris; urutan default Date descending). Alias baris yang dipakai langkah (nilai kolom Field; Modified By dalam format `[First Name] [Last Initial]`):
  - T-1: Field `Manage files — IT Infrastructure`, Modified By `Ahmad D`
  - T-2: Field `Manage group — IT Infrastructure — Delete`, Modified By `Ahmad D`
  - T-3: Field `Manage group — IT Infrastructure — Update`, Modified By `Ahmad D`
  - T-4: Field `Home Group`, Modified By `Lina M`
  - T-5: Field `Manage asset master data — Delete`, Modified By `Ahmad D`
  - T-6: Field `Manage accounting`, Modified By `Ahmad D`
  - T-7: Field `Status`, Modified By `Ahmad D`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed Changelog #27 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface Changelog dan tidak menambah entri pada Budi Santoso.
- Tabel "Kolom Setup Column Hideable" (parameter langkah berulang): Date, Action, Field, Old Value, New Value, Modified By.
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.

## Test Steps

### TC-FA-SU-598: Pin dan unpin Setup Column kelas Hideable

1. Buka Detail pengguna Budi Santoso lalu klik tab Changelog
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
- Langkah berulang per kolom (idiom bagian 8b butir 7): langkah 3 sampai 9 dijalankan 6 kali, satu iterasi per kolom di tabel Prerequisites.
- TC-FA-SU-598 dipetakan ke spec ini; TC lain Setup Column Tab Changelog ada di spec 199 dan 200.
- Spec ini berjumlah 48 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) Post Condition preferensi kolom tersimpan per perangkat tidak punya langkah observasi dan tidak diasersi. (2) TC-FA-SU-598 langkah 3 menyebut pin pada daftar kolom sekaligus, sedangkan Expected g membatasi tiga kolom; spec mem-pin satu kolom per iterasi lalu menguji batas tiga kolom.
