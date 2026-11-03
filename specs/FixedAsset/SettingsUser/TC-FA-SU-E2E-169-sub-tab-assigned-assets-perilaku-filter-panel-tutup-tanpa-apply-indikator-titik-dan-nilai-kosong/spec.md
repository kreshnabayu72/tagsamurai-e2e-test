---
id: TC-FA-SU-E2E-169-sub-tab-assigned-assets-perilaku-filter-panel-tutup-tanpa-apply-indikator-titik-dan-nilai-kosong
title: "Sub-tab Assigned Assets: Perilaku Filter Panel (Tutup Tanpa Apply, Indikator Titik, dan Nilai Kosong)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-455
coverage:
  web: automated
---

# Sub-tab Assigned Assets: Perilaku Filter Panel (Tutup Tanpa Apply, Indikator Titik, dan Nilai Kosong)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook suite dinyatakan di `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup (hanya dibaca, tidak diubah): Client `FaUserMain` (#20) dan Responsibilities (#24): Detail Budi Santoso dengan Sub-tab Assigned Assets 5 baris (satu halaman). Nilai dibaca dari `Fixture.faSettingsUser.preSetup` (fixture belum ada, disediakan tim FE). Pre-setup #24 hanya menyebut "5 baris"; nilai kolom di bawah diturunkan dari Expected TC (Asset ID dan Transaction ID hanya tertulis sebagian):

| Name | Asset ID | Transaction ID | Brand | Model / Type | PIC |
|---|---|---|---|---|---|
| `AC Split Ruang Kerja` | tidak tertulis | tidak tertulis | `Daikin` | `1PK` | `Ahmad D` |
| `Lemari Arsip` | tidak tertulis | tidak tertulis | `Lion` | `2 Pintu` | `Citra L` |
| `Meja Kerja Kepala Divisi` | tidak tertulis | `ASG-20260505` | `Modera` | `Executive` | `Ahmad D` |
| `Printer Multifungsi` | tidak tertulis | tidak tertulis | `Canon` | `PIXMA G3010` | `Citra L` |
| `Server Rack Mini` | `AST-02113` | tidak tertulis | `HP` | `ProLiant DL20` | `Eka W` (Eka Wulandari) |
- Data Dinamis: tidak ada.
- State global: tidak ada yang diubah; spec hanya membaca Pre-setup. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-455: Perilaku Filter Panel Sub-tab Assigned Assets: tutup tanpa Apply, indikator titik, dan nilai kosong

1. Klik nama `Budi Santoso` di User List
2. Klik tab Responsibilities, lalu klik Sub-tab Assigned Assets
3. Klik icon Filter
4. Buka dropdown Name
5. Centang `AC Split Ruang Kerja`
6. Klik di luar panel Filter
7. Verifikasi tabel tidak berubah dan tetap menampilkan seluruh baris
8. Klik icon Filter
9. Verifikasi field Name menampilkan nilai ter-Apply terakhir (kosong, tanpa chip)
10. Buka dropdown Name
11. Centang `AC Split Ruang Kerja`
12. Klik `[Apply]`
13. Klik icon Filter untuk menutup panel
14. Verifikasi ikon Filter menampilkan badge titik saat panel tertutup
15. Klik icon Filter
16. Verifikasi ikon Filter menampilkan badge titik saat panel terbuka
17. Klik `[Clear Field]`
18. Klik `[Apply]`
19. Verifikasi badge titik pada ikon Filter hilang
20. Buka dropdown Name
21. Verifikasi dropdown Name menampilkan opsi nilai lain, antara lain `Lemari Arsip`
22. Verifikasi dropdown Name tidak memiliki opsi untuk nilai kosong
23. Tekan Esc untuk menutup dropdown
24. Centang `AC Split Ruang Kerja`
25. Klik `[Apply]`
26. Klik header Actions (⋯)
27. Uncheck kolom Name pada overlay Column Visibility
28. Verifikasi field Name tetap ada pada panel Filter
29. Verifikasi filter ter-Apply tetap berlaku dan tabel menampilkan satu baris
30. Klik header Actions (⋯)
31. Check kolom Name pada overlay Column Visibility
32. Klik `[Clear Field]`
33. Klik `[Apply]`
34. Klik icon Filter untuk menutup panel

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pembukaan Detail dan sub-tab (langkah 1 dan 2) serta langkah yang mengosongkan Search, Filter, atau popup di antara blok TC supaya blok berikutnya tidak mengandalkan state blok sebelumnya (S-09).
- Pembagian TC lintas spec: TC-FA-SU-453 dan 454 ada di spec 154.
- Temuan untuk QA (S-15):
  - TC-FA-SU-455 Expected c ("memilih opsi apa pun menyaring keluar baris yang nilainya kosong") tidak dapat diasersi: kelima baris Pre-setup #24 tidak memiliki nilai kosong pada kolom Name, Brand, Model / Type, atau PIC. Spec hanya mengasersi bahwa dropdown tidak memiliki opsi untuk nilai kosong.
  - TC-FA-SU-455 Expected d tidak menyebut kolom yang di-hide; spec memakai kolom Name (kolom field Filter yang di-Apply).
