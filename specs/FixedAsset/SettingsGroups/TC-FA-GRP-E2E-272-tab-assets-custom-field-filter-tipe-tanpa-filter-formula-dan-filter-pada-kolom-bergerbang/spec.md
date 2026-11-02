---
id: TC-FA-GRP-E2E-272-tab-assets-custom-field-filter-tipe-tanpa-filter-formula-dan-filter-pada-kolom-bergerbang
title: "Tab Assets Custom Field: Tipe Tanpa Field Filter, Formula Tanpa Search/Sort/Filter, dan Filter pada Kolom Bergerbang Tidak Mencocokkan No Access"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-1274
  - TC-FA-GRP-1275
  - TC-FA-GRP-1276
coverage:
  web: automated
---

# Tab Assets Custom Field: Tipe Tanpa Field Filter, Formula Tanpa Search/Sort/Filter, dan Filter pada Kolom Bergerbang Tidak Mencocokkan No Access

## Prerequisites

- Mode: FE+BE.
- Hook suite: rujuk `suite.md` (login API aktor, sesi API, fixture BE, flag Guided Tooltip `fa-settings-groups` bernilai `seen`).
- Akun aktor pertama: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun (langkah eksplisit, untuk TC-1276): managePurchaseGroups (Pre-setup No 14: Group Role Manage purchase pada Value Gate Node A saja) `managePurchaseGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_MANAGEPURCHASE_PASSWORD`; tidak memegang Manage purchase pada Value Gate Node B.
- Data Pre-setup tambahan (hanya dibaca): Value Gate Node A (Tabel Dinamis No 10, G1-G6), Value Gate Node B (No 11, B1-B3), fixture tipe Custom Field (No 18). Node di-seed idempotent di hook `before` dengan nama bersuffix `{runId}-272` (mekanisme seeding disediakan tim FE/BE). Langkah dan asersi memakai nama bersuffix itu. Asset ID G1-G6 tidak memuat `500`.
- Nilai uji (diacu dari fixture spec): Contact Email G2 `b@x.com`; Usage Hours G2 250 sehingga Computed Total G2 = 500 (Usage Hours x 2, dihitung saat dibaca); Purchase Date B1-B3 `No access` bagi aktor TC-1276.
- General Settings client: Date Format DD/MM/YYYY, Time 24-hour, Timezone Asia/Jakarta (kondisi awal client uji; spec tidak mengubahnya).
- Setup Column: hook `before` menghapus preferensi kolom Tab Assets di browser; hook `after` menghapus preferensi yang disimpan spec (kemampuan disediakan tim FE).
- State global: tidak ada yang diubah.

## Test Steps

### TC-1274: Filter Panel Custom Field bertipe Text, Text Area, Phone, Email, URL, Document tidak punya field Filter
1. Buka Detail Value Gate Node A (Tab Assets)
2. Buka Popup Setup Column
3. Verifikasi kolom Contact Email, Cost Center, dan Computed Total ada di daftar Popup Setup Column
4. Centang kolom Contact Email, Cost Center, dan Computed Total, klik [Save]
5. Klik icon Filter
6. Verifikasi Filter Panel tidak memuat field Contact Email (Email) maupun Cost Center (Text)
7. Verifikasi tidak ada field untuk Computed Total (Formula)
8. Tutup Filter Panel; ketik Search `b@x.com`, tekan Enter
9. Verifikasi G2 tampil (kolom Contact Email tetap dapat dicari lewat Search)
### TC-1275: Kolom Custom Field bertipe Formula (Computed Total) tanpa Search, Sort, maupun Filter
10. Klik `(←)` pada kotak Search
11. Verifikasi header kolom Computed Total tanpa icon Sort
12. Ketik Search `500`, tekan Enter
13. Verifikasi empty state Illustration, title "No results found", body "Try adjusting your search or filter." (hasil formula G2 tidak menemukan baris dari kolom ini)
14. Klik icon Filter
15. Verifikasi Filter Panel tidak memuat field Computed Total
### TC-1276: Filter pada kolom Custom Field bergerbang: baris `No access` tidak cocok dengan filter apa pun
16. Ganti akun: Logout, login sebagai managePurchaseGroups (`managePurchaseGroups_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_GRP_MANAGEPURCHASE_PASSWORD`), buka Fixed Asset > Settings > Groups
17. Buka Detail Value Gate Node B (Tab Assets)
18. Klik icon Filter; pada field Purchase Date pilih rentang 01/01/2020-31/12/2035, klik [Apply]
19. Verifikasi empty state Illustration, title "No results found", body "Try adjusting your search or filter." (Purchase Date B1-B3 `No access` tidak cocok filter apa pun)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): pada TC-1274, Popup Setup Column dibuka dan ketiga kolom dicentang sebelum Filter Panel dibuka (urutan langkah TC dibalik karena kolom harus tampil dahulu); "Tutup Filter Panel" sebelum Search; satu langkah Ganti akun sebelum TC-1276.
- Asersi tambahan (S-03): `Verifikasi` Search `b@x.com` menampilkan G2 pada TC-1274 menerjemahkan klausa Expected a "kolom tetap dapat dicari lewat Search", yang tidak punya langkah di TC; nilai `b@x.com` dari TC-1268. `Verifikasi` ketiga kolom ada di Popup Setup Column adalah anchor positif untuk asersi absence field Filter (8b butir 2).
- Temuan untuk QA:
  - TC-1274 langkah 4 dan Expected a tidak menjelaskan cara membuktikan "kolom tetap dapat dicari lewat Search"; spec menambah langkah Search seperti di atas.
  - TC-1275 Expected b "tidak menemukan baris dari kolom ini" tidak menyebut keyword; spec memakai hasil formula G2 (Usage Hours 250 x 2 = 500) dan mengasumsikan empty state karena kolom lain tidak memuat `500`.
  - TC-1274 berlabel FE Test "UI Only" sedangkan data Tabel Dinamis No 18 di-seed backend; spec tetap `FE+BE`.
