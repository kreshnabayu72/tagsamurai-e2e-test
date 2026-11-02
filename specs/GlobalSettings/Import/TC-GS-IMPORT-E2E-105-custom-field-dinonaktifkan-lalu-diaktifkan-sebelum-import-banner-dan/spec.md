---
id: TC-GS-IMPORT-E2E-105-custom-field-dinonaktifkan-lalu-diaktifkan-sebelum-import-banner-dan
title: "Custom Field dinonaktifkan lalu diaktifkan sebelum Import: banner dan nilai ikut ditulis ke User"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-971
coverage:
  web: automated
---

# Custom Field dinonaktifkan lalu diaktifkan sebelum Import: banner dan nilai ikut ditulis ke User

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena spec menjalankan commit di Client E, mengubah status Custom Field `Shift`, dan memakai kontrol worker commit (lihat `suite.md`). Client E khusus commit (Kontrak Fixture R3); tidak ada spec lain berjalan pada Client E bersamaan.
- Akun aktor (login sekali di hook `before`): Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTE_TC_PASSWORD` (nama env baru, didaftarkan pada tahap script).
- Pelaku kedua (hanya memicu perubahan state lewat sesi API, tanpa asersi UI di sesinya, P-2): Admin kedua Client E (Dimas Anggoro) `totalControlSecond_automated_qaTeam5@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTE_TC2_PASSWORD` (nama env baru); klien HTTP disediakan tim FE/BE. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Import > User Login untuk Client E.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini, lihat `suite.md`.
- Data Pre-setup Client E: produk Global Settings dan Fixed Asset; Custom Field `Shift` (Dropdown Pagi, Siang, Malam) Active; master data seperti Client A (Email User bersufiks `.e`).
- Data Dinamis: D-54 (Draft User Login 8 baris `pending` di Client E dari `user-login-commit-8.csv`: Rizky Pratama (EMP-5001, Shift `Siang`), Sinta Maharani (Active Period H+30, Shift `Siang`), Doni Kurniawan (Finance Manager, Shift `Pagi`), Eka Putri (Overtime Hours 1.25), Fajar Hidayat, Gita Savitri, Hendra Gunawan, Indah Permata; isi lengkap pada Data Uji TC-GS-IMPORT-356), disiapkan oleh langkah 1 lewat skrip fixture (Kontrak Fixture R1 dan R2); Shift `Siang` pada Row # 1 dan 2, `Pagi` pada Row # 3. Nama dan Employee ID literal karena asersi bergantung pada isi D-54.
- Kontrol worker commit: mode normal (worker berjalan tanpa jeda); disediakan tim FE/BE (D-47).
- Kemampuan teknis: sesi API Admin kedua untuk menonaktifkan dan mengaktifkan Custom Field `Shift`; muat ulang halaman berkala tiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit); skrip pembersihan hasil commit (disediakan tim FE/BE).
- State global: Custom Field `Shift` Client E dinonaktifkan lalu diaktifkan kembali oleh Admin kedua; 8 user hasil commit tercipta di Client E. Hook `after` memulihkan Custom Field `Shift` ke Active dengan opsi Pre-setup, menghapus 8 user hasil commit (D-47), dan membuang draft/penanda Banner Hasil Commit walau spec gagal di tengah.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): seperti di atas.

## Test Steps

### TC-GS-IMPORT-971: Custom Field dinonaktifkan lalu diaktifkan kembali sebelum Import

1. Seed draft User Login D-54 (8 baris, `user-login-commit-8.csv`) di Client E lewat skrip fixture; muat ulang halaman Import > User Login
2. Admin kedua Client E menonaktifkan Custom Field `Shift` lewat sesi API hingga tersimpan
3. Tekan F5 pada halaman Import > User Login
4. Verifikasi Banner Custom Field Deactivated tampil dengan teks "Shift is deactivated. Its values stay hidden on users until it is activated."
5. Admin kedua Client E mengaktifkan kembali Custom Field `Shift` lewat sesi API hingga tersimpan
6. Tekan F5 pada halaman Import > User Login
7. Verifikasi kolom Shift tetap bernilai `Siang` pada Row # 1
8. Verifikasi kolom Shift tetap bernilai `Siang` pada Row # 2
9. Verifikasi Banner Custom Field tidak tampil
10. Klik `[Import (8)]`
11. Tunggu aksi selesai (permintaan mendapat respons)
12. Muat ulang halaman Import > User Login setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
13. Verifikasi Banner Hasil Commit bertone success: "Success, record has been imported. Duplicate records were ignored."
14. Buka halaman User > User List > Login User dan atur Rows per page 100
15. Buka Detail user `Rizky Pratama`
16. Verifikasi Detail user `Rizky Pratama` menampilkan Custom Field Shift bernilai `Siang`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fungsional (worker commit mode normal dan Admin kedua hanya pemicu, P-2).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1 (seed draft D-54 dan muat ulang halaman); langkah 11 (menunggu permintaan commit mendapat respons); langkah 12 (menunggu commit selesai dengan memuat ulang halaman berkala, Langkah 6 TC sumber); langkah 14 (membuka User List, Langkah 7).
- Penyimpangan urutan dari Expected b TC: Verifikasi kolom Shift (langkah 7 dan 8) mendahului asersi Banner tidak tampil (langkah 9) supaya absence sesudah `F5` punya anchor positif (butir 2 bagian 8b).
- Spec satu TC; tidak digabung dengan spec commit lain karena Custom Field dinonaktifkan di Client E dan commit berjalan sendiri.
- Pembagian TC lintas spec: TC-GS-IMPORT-356 (Dependensi; commit User Login Client E) berada di spec commit lain.
- Temuan untuk QA:
  - TC-GS-IMPORT-971 menyebut Dependensi TC-GS-IMPORT-356; spec menyiapkan D-54 sendiri lewat skrip fixture dan tidak menumpang hasil TC lain (S-04).
  - Nilai waktu uji "2 menit" ditandai `PRD?` pada dump TC (tidak ada di PRD); batas tunggu itu pilihan TC sendiri, bukan aturan PRD.
  - TC-GS-IMPORT-971 Post Condition a-b ("Fixture dipulihkan", "8 user hasil commit dihapus") dikerjakan hook `after` dan tidak diasersi (S-01). Mekanisme Admin kedua menonaktifkan Custom Field (UI atau API) tidak disebut TC; spec memakai sesi API (P-2).
