---
id: TC-FA-FAAC-E2E-090-unassign-menu-baris-dialog-dan-blokir
title: "Unassign: Menu Baris Asset Name, Dialog Single, dan Blokir Asset Name dengan Aset Aktif"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-228
  - TC-FA-FAAC-229
  - TC-FA-FAAC-230
  - TC-FA-FAAC-235
sourceRules: ["§4.1.3#p5", "§3.9#r13", "§4.3#p1", "ST-11", "§3.9#r15", "D-15", "D-17", "F-FAAC-10.k1", "R-11"]
smoke: []
dependsOn: []
trace:
  "§4.1.3#p5": [5, 11]
  "§3.9#r13": 5
  "§4.3#p1": 7
  "ST-11": [11, 12]
  "§3.9#r15": 13
  "D-15": 16
  "D-17": 23
  "F-FAAC-10.k1": 27
  "R-11": 28
anchor: [18, 19, 20, 25, 26]
coverage:
  web: automated
---

# Unassign: Menu Baris Asset Name, Dialog Single, dan Blokir Asset Name dengan Aset Aktif

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed (kode dan nama literal TC, disediakan tim FE/BE lewat fixture BE): Asset Class Active `Heavy Equipment` (`HEAVY-EQ`) dengan Asset Name ter-assign `Excavator PC200` (8 aset aktif), `Wheel Loader` (4 aset aktif), dan `Crane Rental Unit` (0 aset aktif). Spec ini hanya membuka menu dan dialog lalu membatalkannya, tidak mengubah data.
- Kode seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada nama dan jumlah aset aktif itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Ketik Search `HEAVY-EQ`, tekan Enter
2. Klik link Class Code `HEAVY-EQ` di tabel
3. Klik tab `Asset Names`

### TC-FA-FAAC-228: Menu baris Asset Name tanpa aset aktif memuat Move dan Unassign yang Enabled

4. Klik ikon `⋯` pada baris `Crane Rental Unit`
5. Verifikasi menu memuat `Move` dan `Unassign`, keduanya tampil dan Enabled
6. Arahkan kursor ke `Unassign`
7. Verifikasi `Unassign` tanpa tooltip
8. Tekan `Esc` untuk menutup menu

### TC-FA-FAAC-229: Unassign Disabled untuk Asset Name dengan aset aktif beserta tooltip

9. Klik ikon `⋯` pada baris `Excavator PC200`
10. Arahkan kursor ke `Unassign` lalu coba klik
11. Verifikasi `Unassign` tetap tampil (visible) namun Disabled dengan tooltip `Move this asset name instead. It still has active assets.`
12. Verifikasi `Unassign` tidak dapat diklik dan tidak ada dialog yang terbuka
13. Verifikasi `Move` tampil dan Enabled
14. Tekan `Esc` untuk menutup menu

### TC-FA-FAAC-230: Dialog konfirmasi Unassign single menampilkan copy lengkap dan Cancel tidak mengubah data

15. Klik ikon `⋯` pada baris `Crane Rental Unit`, lalu pilih `Unassign`
16. Verifikasi Dialog `Unassign Asset Name` berisi `• Crane Rental Unit` dan `It will have no asset class and its assets will not be depreciated. Are you sure you want to unassign it?` dengan footer `[Cancel]` dan `[Unassign]` (severity danger)
17. Klik `[Cancel]`
18. Verifikasi tidak ada toast yang tampil
19. Verifikasi dialog menutup
20. Verifikasi `Crane Rental Unit` tetap tampil di tab Asset Names

### TC-FA-FAAC-235: Unassign massal semua Asset Name memiliki aset aktif menampilkan Dialog Blok

21. Centang baris `Excavator PC200` dan `Wheel Loader`
22. Klik `Bulk Action`, lalu pilih `Unassign`
23. Verifikasi Dialog Blok `Cannot Unassign Asset Names` berisi `• Excavator PC200 — has active assets`, `• Wheel Loader — has active assets`, dan `These asset names still have active assets. Move them to another asset class instead.` dengan tombol `[OK]`
24. Klik `[OK]`
25. Verifikasi tidak ada toast yang tampil
26. Verifikasi dialog menutup
27. Verifikasi tidak ada perubahan: `Excavator PC200` dan `Wheel Loader` tetap tampil di tab Asset Names
28. Verifikasi seleksi dipertahankan: kedua baris tetap tercentang
29. Klik `Unselect All`
30. Klik `(←)` pada kotak Search

## Notes

1. Urutan dalam spec: screening menu baris (TC-228, TC-229), dialog single dengan batal (TC-230), lalu blokir massal (TC-235); semua pada Detail `HEAVY-EQ` yang sama, dibuka sekali di langkah 2 dan 3.
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 (Search untuk menemukan baris target, R-16), langkah 8 dan 14 (menutup menu), langkah 17 dan 24 (menutup dialog), langkah 29 (membersihkan seleksi, S-09), dan langkah 30 (mengosongkan Search).
3. Pengecualian kode seed literal: TC mewajibkan Asset Class dan Asset Name seed bernama literal dengan jumlah aset aktif tertentu; dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini). Aksi hanya dibatalkan atau ditolak sehingga data tidak berubah.
4. Pembagian TC: TC-234 dan TC-239 (Unassign pada Asset Class lain) ada di spec 110.
5. Temuan untuk QA: Tabel Data Uji Pre-setup TC hanya memuat akun fixture; data seed Asset Class dan Asset Name hanya tertulis di Precondition tiap TC. Post Condition tidak ada pada keempat TC.
