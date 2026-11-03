---
id: TC-AC-DS-E2E-151-log-absence-tanpa-perubahan-ditolak-dan-promosi-default
title: "Absence Log: Edit Tanpa Perubahan dan Edit Field Terkunci yang Ditolak Tidak Menulis Log"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-206
  - TC-AC-DS-482
  - TC-AC-DS-484
coverage:
  web: automated
---

# Absence Log: Edit Tanpa Perubahan dan Edit Field Terkunci yang Ditolak Tidak Menulis Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca, tidak diubah): SKU inti `HHR-ARC-200` dan `HHR-ARC-100` (field SKU terkunci karena stok 120) serta seed (#29, #30), pohon Category (#25), Device Name (#26), Brand Principal (#27), file foto uji (#37), General Settings Date Format `dd/MM/yy`, 24 jam, Asia/Jakarta (#35), riwayat Changelog Principal (#33). Nilai dibaca dari `Fixture.settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE). Last Modified `HHR-ARC-200` dibaca saat run (T) sebelum `[Save]` dan dibandingkan sesudahnya, bukan literal Pre-setup. Ketiga aksi tidak mengubah data (tanpa perubahan atau ditolak), sehingga Last Modified dan jumlah entri tetap.
- Data Dinamis: tidak ada.
- Kemampuan teknis (disediakan tim FE/BE): pembacaan jumlah entri (baseline) Changelog Principal, System Log aktor `Jane Setiawan`, dan Activity Log tab User Action untuk SKU terkait sebelum aksi (audit trail permanen; 8b butir 10); menghapus atribut `disabled` pada field SKU lewat DevTools (manipulasi DOM) di browser uji.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

1. Ketik Search `HHR-ARC-200`, tekan Enter

### TC-AC-DS-206: Save tanpa perubahan menampilkan toast netral dan tidak menulis log

2. Catat Last Modified baris `HHR-ARC-200` sebagai T
3. Klik ⋯ pada baris `HHR-ARC-200`, pilih `Edit`
4. Verifikasi Popup Edit SKU tampil dengan field terisi
5. Klik `[Save]` tanpa mengubah field apa pun
6. Verifikasi toast info "No changes to save." tampil
7. Verifikasi tidak ada pesan duplikat SKU terhadap dirinya sendiri
8. Verifikasi Popup Edit tertutup
9. Verifikasi Last Modified baris `HHR-ARC-200` tetap sama dengan T (langkah 2)

### TC-AC-DS-482: Edit tanpa perubahan tidak menulis entri pada Changelog, System Log, maupun Activity Log

10. Catat baseline jumlah entri Changelog, System Log aktor `Jane Setiawan`, dan Activity Log tab User Action untuk `HHR-ARC-200`
11. Klik ⋯ pada baris `HHR-ARC-200`, pilih `Edit`
12. Klik `[Save]` tanpa mengubah field apa pun
13. Verifikasi toast info "No changes to save." tampil
14. Klik ikon Changelog
15. Verifikasi modal "Changelog: Device SKU" tampil
16. Verifikasi jumlah entri Changelog untuk `HHR-ARC-200` tidak bertambah dari baseline langkah 10
17. Buka Settings > User, cari user `totalControlSku_automated_{namaCompany}@qwertysystem.net`, buka Detail, buka tab System Log
18. Verifikasi jumlah entri System Log aktor `Jane Setiawan` untuk `HHR-ARC-200` tidak bertambah dari baseline langkah 10
19. Buka Activity Log, buka tab User Action
20. Verifikasi jumlah entri Activity Log untuk `HHR-ARC-200` tidak bertambah dari baseline langkah 10

### Pemulihan state antar TC

21. Buka Settings > Device > Device SKU

### TC-AC-DS-484: Edit field terkunci yang ditolak tidak menulis entri log

22. Ketik Search `HHR-ARC-100`, tekan Enter
23. Catat baseline jumlah entri Changelog untuk `HHR-ARC-100`
24. Klik ⋯ pada baris `HHR-ARC-100`, pilih `Edit`
25. Verifikasi Popup Edit SKU tampil dengan field terisi
26. Hapus atribut `disabled` pada field SKU lewat DevTools, lalu ubah SKU menjadi `HHR-ARC-199`
27. Klik `[Save]`
28. Verifikasi toast error "Error, failed to update device SKU." tampil
29. Klik ikon close `[✕]` Popup Edit SKU
30. Verifikasi dialog `Unsaved Changes` tampil
31. Klik `[Leave]`
32. Klik ikon Changelog
33. Verifikasi modal "Changelog: Device SKU" tampil
34. Verifikasi Changelog tidak menambah entri baru untuk `HHR-ARC-100` (jumlah entri sama dengan baseline langkah 23)

### Pemulihan state akhir

35. Tutup modal Changelog; klik `(←)` pada kotak Search

## Notes

- P-5: spec ini adalah spec absence (kelas g, bagian 3 prinsip 13 butir g). Pemicu kelas a pada TC-AC-DS-484 (menghapus atribut `disabled` lewat DevTools lalu Save) hanya membentuk kondisi yang diasersi tidak tercatat, bukan objek uji; tiap TC punya baseline sendiri (langkah 10, 23).
- Asersi absence didahului anchor positif (8b butir 2): toast info hasil server (langkah 6 dan 13) dan toast error hasil server (langkah 28), serta modal Changelog yang tampil (langkah 15 dan 33), sebelum membandingkan jumlah entri dengan baseline.
- Langkah penghubung tanpa `Verifikasi`: langkah 1 dan 22 (Search untuk menemukan baris target, R-16), langkah 2 dan 10 dan 23 (pencatatan Last Modified T dan baseline, S-12), langkah 21 dan 35 (S-03, S-09). Dialog `Unsaved Changes` pada langkah 30 mengikuti S-08.
- Last Modified `HHR-ARC-200` dibaca saat run (langkah 2) dan dibandingkan sesudah Save (langkah 9), bukan literal Pre-setup, karena nilai Last Modified Pre-setup bergantung pada pemulihan fixture BE antar spec (A-11).
- Pengecualian S-12 A-11: `HHR-ARC-200` dan `HHR-ARC-100` adalah SKU Pre-setup bernama literal tanpa suffix (dinyatakan di `suite.md`); tidak ada data yang diubah spec ini. `HHR-ARC-199` hanya diketik pada penolakan dan tidak pernah tersimpan.
- TC-AC-DS-478, TC-AC-DS-495, TC-AC-DS-515, TC-AC-DS-520, dan TC-AC-DS-523, yang juga bersifat absence, ada di spec 193.
- Post Condition TC-AC-DS-206 ("tidak ada entri baru di Changelog, System Log aktor, maupun Activity Log") tanpa langkah observasi di TC 206; ditutup oleh TC-AC-DS-482 yang memiliki aksi nyata dan baseline sendiri pada `HHR-ARC-200` (S-05).
- Temuan untuk QA:
  - S-15: TC 482 langkah 3 ("catat jumlah entri ... untuk `HHR-ARC-200`") tidak menyebut cara mencatat; spec memakai kemampuan baca baseline dan membandingkan jumlah pada tiap surface sesudah Save.
  - S-15: TC 484 langkah 5 ("tutup popup") tidak menyebut dialog `Unsaved Changes` pada form dirty; spec mengikuti S-08 (✕, dialog, `[Leave]`).
  - S-13: pencarian user di Settings > User memakai email bersuffix `{namaCompany}`; TC hanya menyebut nama `Jane Setiawan`.
  - Fixture rancangan Pre-setup #33 belum terverifikasi ada di environment; `Fixture.settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
