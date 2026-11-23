---
id: TC-FA-FAAC-E2E-207-create-end-of-life-treatment-commercial-opsi-nilai-awal-dan-clear-field
title: "Create Asset Class: End-of-Life Treatment Commercial Muncul pada Declining Balance dengan Tiga Opsi dan Nilai Awal, Hilang dan Pulih Lewat Clear Field"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-719
  - TC-FA-FAAC-722
sourceRules: ["FLD-33", "FAAC-LOGIC-02h", "ST-08", "FI-01"]
smoke: []
dependsOn: []
trace:
  "FLD-33": [6, 7, 9, 17]
  "FAAC-LOGIC-02h": [4, 6, 7, 15, 17]
  "ST-08": [4, 6, 15, 17]
  "FI-01": [4, 6, 15, 17]
coverage:
  web: automated
---

# Create Asset Class: End-of-Life Treatment Commercial Muncul pada Declining Balance dengan Tiga Opsi dan Nilai Awal, Hilang dan Pulih Lewat Clear Field

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Pre-setup: tidak ada yang dipakai selain akun aktor. Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` bila diperlukan (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Data Dinamis: tidak ada. Spec hanya membuka form Create, memilih Method, dan mengubah End-of-Life Treatment tanpa Submit sehingga tidak ada Asset Class yang dibuat dan tidak ada cleanup.
- Kemampuan teknis: tidak ada selain browser.
- State global: tidak ada yang diubah. Form Create ditutup lewat klik breadcrumb `Asset Class` pada akhir spec.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di `suite.md`.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### Persiapan

1. Klik tombol `+ Asset Class` di toolbar tabel
2. Klik tab `Depreciation`

### TC-FA-FAAC-719: Pilih Method Declining Balance menampilkan End-of-Life Treatment dengan tiga opsi dan nilai awal Switch to straight-line

3. Verifikasi kartu Commercial tampil
4. Verifikasi field End-of-Life Treatment tidak tampil sebelum Method dipilih
5. Pilih Method `Declining Balance`
6. Verifikasi field End-of-Life Treatment tampil sebagai select tunggal dengan indikator wajib pada label
7. Verifikasi End-of-Life Treatment sudah bernilai `Switch to straight-line` (bukan kosong)
8. Buka select End-of-Life Treatment
9. Verifikasi opsi select persis tiga: `Charge in final period`, `Switch to straight-line`, `Keep depreciating`
10. Tutup select End-of-Life Treatment tanpa mengubah pilihan

### TC-FA-FAAC-722: Clear Field pada Create Declining Balance menyembunyikan End-of-Life Treatment dan memulihkan nilai awal saat Declining Balance dipilih lagi

11. Ubah End-of-Life Treatment menjadi `Keep depreciating`
12. Klik `[Clear Field]` di footer
13. Verifikasi Method belum terpilih (placeholder `Select method`)
14. Verifikasi tidak ada dialog apa pun yang tampil
15. Verifikasi field End-of-Life Treatment tidak tampil
16. Pilih Method `Declining Balance` lagi
17. Verifikasi End-of-Life Treatment bernilai `Switch to straight-line` (bukan `Keep depreciating`)
18. Klik breadcrumb `Asset Class`
19. Verifikasi dialog `Unsaved Changes` tampil karena Method telah dipilih sehingga isian berbeda dari kondisi awal form
20. Klik `[Leave]`
21. Verifikasi tabel Asset Class tampil

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-719, TC-FA-FAAC-722). Tidak ada TC hanya-BE di spec ini. Keduanya bertanda UI Only; spec tetap `Mode: FE+BE` karena dijalankan di suite FE+BE.
- Satu pembukaan form dipakai bersama untuk dua TC (prinsip 6 dan 8, halaman yang sama dipakai berulang): langkah 1 sampai 2 identik di kedua TC, dan Method `Declining Balance` sudah dipilih pada langkah 5 sehingga langkah TC-722 "pilih Method Declining Balance" tidak diulang sebelum langkah 11. Form hanya ditutup sekali (langkah 18 sampai 20).
- Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 10 (menutup select tanpa mengubah pilihan). Langkah 3 dan 13 adalah anchor positif asersi absence pada langkah 4, 14, dan 15 (bagian 8b butir 2); langkah 3 tidak ada di Expected TC dan ditambahkan hanya sebagai anchor kartu Commercial sudah termuat (S-03).
- Verifikasi dialog `Unsaved Changes` pada langkah 19 menjalankan S-08 sekaligus Expected TC-722 butir c.
- Temuan untuk QA: (a) TC-722 tidak menyebut Tab apa pun sesudah Clear Field selain Method placeholder; spec mengasersi Method belum terpilih dan field End-of-Life Treatment tidak tampil sesuai Expected butir a. (b) TC-719 butir b menyebut "indikator wajib pada label" tanpa bentuk visualnya; spec mengasersi indikator wajib tanpa mengarang simbol.
