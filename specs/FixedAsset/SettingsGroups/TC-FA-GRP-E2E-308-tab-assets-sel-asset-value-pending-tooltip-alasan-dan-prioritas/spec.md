---
id: TC-FA-GRP-E2E-308-tab-assets-sel-asset-value-pending-tooltip-alasan-dan-prioritas
title: "Tab Assets Sel Asset Value Pending: Tooltip Alasan Purchase Cost Belum Diisi atau Asset Class Belum Diisi dan Prioritas Alasan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1305
coverage:
  web: automated
---

# Tab Assets Sel Asset Value Pending: Tooltip Alasan Purchase Cost Belum Diisi atau Asset Class Belum Diisi dan Prioritas Alasan

## Prerequisites

- Mode: FE+BE.
- Akun Total Control (Pre-setup No 1): `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`) berlaku: sesi API aktor, fixture BE, flag Guided Tooltip `seen`, dan pemulihan state global; tidak ditulis ulang di sini.
- Data Value Gate Node D (Tabel Dinamis No 25, hanya dibaca, tidak diubah; Pre-setup tambahan baru, fixture disediakan tim FE/BE): group Assignable level 1 berisi hanya aset D1 `Unclassed - 1` (Asset Name `Unclassed Item` tanpa Asset Class; Purchase Cost 1000) dan D2 `Unclassed - 2` (Asset Name sama; tanpa Purchase Cost).
- Kemampuan teknis: menghapus preferensi kolom Setup Column di browser (disediakan tim FE).
- Preferensi kolom Setup Column yang disimpan spec ini dihapus dari browser di hook `after` (kemampuan disediakan tim FE).
- State global: tidak ada yang diubah. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-GRP-1305: Sel Asset Value Pending: tooltip alasan Purchase cost belum diisi atau Asset class belum diisi, dan prioritas alasan

1. Ketik Search `Value Gate Node D` pada Groups List, tekan Enter
2. Buka Detail Value Gate Node D (Tab Assets)
3. Buka Popup Setup Column
4. Centang `Asset Value (Commercial)` dan `Asset Value (Fiscal)`, klik [Save]
5. Verifikasi D1 dan D2 menampilkan teks `Pending` pada kedua kolom (bukan `—`, bukan currency nol, bukan `No access`)
6. Hover sel `Pending` D1 pada kolom `Asset Value (Commercial)`
7. Verifikasi tooltip D1 pada kolom `Asset Value (Commercial)`: `Asset class has not been set.` (Purchase Cost ada, Asset Class belum ada)
8. Hover sel `Pending` D1 pada kolom `Asset Value (Fiscal)`
9. Verifikasi tooltip D1 pada kolom `Asset Value (Fiscal)`: `Asset class has not been set.`
10. Hover sel `Pending` D2 pada kolom `Asset Value (Commercial)`
11. Verifikasi tooltip D2 pada kolom `Asset Value (Commercial)`: `Purchase cost has not been set.` (Purchase Cost dan Asset Class sama-sama belum ada; prioritas alasan Purchase)
12. Hover sel `Pending` D2 pada kolom `Asset Value (Fiscal)`
13. Verifikasi tooltip D2 pada kolom `Asset Value (Fiscal)`: `Purchase cost has not been set.`
14. Verifikasi tooltip sel `Pending` tidak memuat metode atau masa manfaat
15. Buka Popup Setup Column, hilangkan centang `Asset Value (Commercial)` dan `Asset Value (Fiscal)`, klik [Save]

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): menghilangkan centang kedua kolom di akhir agar kolom tidak tersimpan; hover `Pending` pada langkah TC 5 dipecah per sel dan per kolom (langkah 6, 8, 10, 12) agar tooltip tiap sel diverifikasi.
- Langkah penghubung (S-03, S-14, R-16): sebelum `Buka Detail` ditambahkan Search Groups List dengan nama group target (`Value Gate Node D`), karena client memiliki lebih dari 10 node level 1 dan page size 10 sehingga baris target tidak dijamin berada di halaman 1.
- Temuan untuk QA:
  - TC-FA-GRP-1305 butir e (pemanggil tanpa hak melihat `No access`, bukan `Pending`) merujuk TC-FA-GRP-1216 dan tidak diasersi di spec ini; asersi itu ada di spec TC-FA-GRP-E2E-256.
  - Value Gate Node D (Tabel Dinamis No 25) adalah fixture baru; kunci fixture belum ada dan disediakan tim FE/BE.
  - Post Condition TC tidak disebut; tidak diasersi.
