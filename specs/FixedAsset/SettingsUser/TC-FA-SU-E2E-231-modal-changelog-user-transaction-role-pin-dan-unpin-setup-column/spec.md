---
id: TC-FA-SU-E2E-231-modal-changelog-user-transaction-role-pin-dan-unpin-setup-column
title: "Modal Changelog User > Transaction Role: Pin dan Unpin Setup Column"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-694
coverage:
  web: automated
---

# Modal Changelog User > Transaction Role: Pin dan Unpin Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Changelog (#27). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Modal Changelog Budi Santoso > Transaction Role (Pre-setup #27, 5 baris; urutan default Date descending). Alias baris yang dipakai langkah (nilai kolom Field; Modified By):
  - TR-1: `Damaged — Branch Surabaya — Monitoring & Report`; Modified By `Ahmad D`
  - TR-2: `Missing — Branch Surabaya — Approver`; Modified By `Ahmad D`
  - TR-3: `Disposal — Logistics Warehouse — Asset Admin`; Modified By `Lina M`
  - TR-4: `Disposal — Logistics Warehouse — Staff`; Modified By `Lina M`
  - TR-5: `Transfer — Finance & Accounting — Asset Admin`; Modified By `Ahmad D`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed Changelog #27 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface Changelog dan tidak menambah entri pada Budi Santoso.
- Tabel "Kolom Setup Column Hideable" (parameter langkah berulang): Date, Action, Field, Old Value, New Value, Modified By.
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.
- Kemampuan teknis: viewport browser dipersempit agar tabel dapat di-scroll horizontal (disediakan tim FE).

## Test Steps

### TC-FA-SU-694: Pin dan unpin Setup Column kelas Hideable

1. Ketik Search `Budi Santoso`, tekan Enter, lalu buka Detail pengguna Budi Santoso, klik tab Role, klik sub-tab Transaction Role, lalu klik icon Changelog
2. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" (langkah 3 sampai 9):
3. Buka Setup Column lalu klik icon Pin pada kolom tersebut
4. Klik `[Save]`, lalu scroll tabel secara horizontal
5. Verifikasi kolom tersebut membeku di kiri saat tabel di-scroll horizontal
6. Klik F5, lalu scroll tabel secara horizontal
7. Verifikasi kolom tersebut tetap membeku di kiri setelah refresh (F5)
8. Buka Setup Column lalu unpin kolom tersebut, klik `[Save]`, lalu scroll tabel secara horizontal
9. Verifikasi kolom tersebut terlepas (tidak lagi membeku) saat tabel di-scroll horizontal
10. Buka Setup Column lalu klik icon Pin pada tiga kolom pertama
11. Hover icon Pin kolom lain yang disabled
12. Verifikasi icon Pin kolom lain disabled dengan tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
13. Klik `[✕]` pada Setup Column untuk membuang perubahan
14. Hapus preferensi kolom tabel di browser lalu muat ulang halaman (kemampuan disediakan tim FE)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung (S-03, R-16): Search `Budi Santoso` pada User List menyaring baris target sebelum membuka Detail (langkah 1) karena User List dapat memuat lebih dari satu halaman (bagian 8b butir 13); langkah ini tidak mengubah data dan tidak ada TC berikutnya yang membutuhkan tabel penuh (S-09).
- Langkah penghubung tambahan (S-03): langkah 11 (Hover icon Pin kolom lain yang disabled) hanya memunculkan tooltip sebelum `Verifikasi` tooltip pada langkah 12 (bagian 8b butir 5); tidak ada asersi.
- TC lain Setup Column modal Transaction Role ada di spec 227 dan 228.
- Langkah berulang per kolom (idiom bagian 8b butir 7): langkah 3 sampai 9 dijalankan 6 kali, satu iterasi per kolom di tabel Prerequisites.
- Spec ini berjumlah 49 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) Post Condition preferensi kolom tersimpan per perangkat tidak punya langkah observasi dan tidak diasersi. (2) TC-FA-SU-694 langkah 3 menyebut pin pada daftar kolom sekaligus, sedangkan Expected g membatasi tiga kolom; spec mem-pin satu kolom per iterasi lalu menguji batas tiga kolom. (3) TC tidak menyebut apakah modal Changelog tetap terbuka setelah F5; spec mengikuti TC (Klik F5 lalu Verifikasi pada tabel modal) dan pembukaan ulang modal bila perlu ditentukan skrip uji.
