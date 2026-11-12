---
id: TC-AC-ACAL-E2E-042-volume-besar-download-1048577-baris-retensi-lintas-tahun-dan-browsing-10000
title: "Volume Besar: Download 1.048.577 Baris, Retensi Lintas Tahun, dan Browsing 10.000 Entri"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACAL-158
  - TC-AC-ACAL-159
  - TC-AC-ACAL-171
coverage:
  web: automated
---

# Volume Besar: Download 1.048.577 Baris, Retensi Lintas Tahun, dan Browsing 10.000 Entri

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Volume khusus spec ini (`Fixture.activityLog.akunVolume042`, disediakan tim FE; email tidak tertulis di Pre-setup TC, lihat Temuan untuk QA), kredensial `Spectra.env.AC_VOLUME_TC_PASSWORD` (nama env usulan tim FE yang belum terdaftar di `.env.example` maupun `spectra.config.ts`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Entitas ini dipakai hanya oleh spec ini karena seed volume tidak dapat dihapus dan akan mengubah jumlah baris di spec lain. Password tidak ditulis di spec atau fixture. Spec tidak mengganti akun.
- Guided Tooltip: hook `before`/`after` spec ini menyetel dan memulihkan flag seen untuk akun `akunVolume042` dan halaman Admin Console > Activity Log (kemampuan disediakan tim FE/BE).
- Data volume (kelas volume data, bagian 3 prinsip 13e), disediakan lewat seed BE di entitas Volume sebelum run (mekanisme seeding log tidak disebut TC, PRD, atau LLD; disediakan tim FE/BE):
  - Tab User Action: 1.048.577 entri dalam scope sesuai TC (seeding; TC-AC-ACAL-171). Jumlah sebenarnya dibaca sebagai Z dari footer `Showing X–Y of Z entries` tab User Action pada langkah 13, sebelum Download; Z lebih dari 1.048.575 sehingga unduhan XLSX terbagi dua sheet. Di antaranya sedikitnya 10.000 entri Name `Entri Volume {runId}-042 NNNNNNN` dengan Action `Create` dan Object `Brand` (TC-AC-ACAL-159) serta entri retensi di bawah (dihitung dalam total).
  - Retensi lintas tahun (TC-AC-ACAL-158), bersuffix `{runId}-042`: baris Session user `Uji Retensi {runId}-042` bercap `18 Jun 2024` (jam bebas) dan entri User Action Name `Entri Retensi {runId}-042` bercap `18 Jun 2024` (jam bebas).
  - Pembersihan: baris log tidak dapat dihapus lewat UI atau API modul ini; entitas Volume direset oleh tim BE di luar spec.
- Tabel "Aksi browsing User Action" (TC-AC-ACAL-159), dipakai langkah 7 sampai 11:

  | No | Aksi |
  |---|---|
  | 1 | Klik menu Activity Log di sidebar, lalu klik tab "User Action" |
  | 2 | Ketik Search `Entri Volume {runId}-042`, tekan Enter |
  | 3 | Klik icon Filter, buka dropdown Action, centang `Create`, klik [Apply] |
  | 4 | Klik icon sort pada header kolom Name sekali (ascending) |

- Kemampuan teknis (disediakan tim FE/BE):
  - Menangkap berkas unduhan browser ke direktori bersih per unduhan; membaca isi XLSX (nama sheet, baris header, jumlah baris data per sheet) dan CSV (jumlah baris data) pada berkas berukuran sangat besar. Berkas unduhan dihapus di hook `after`.
  - Mengamati loading screen penuh dan loading component biasa secara tepat waktu (muncul atau tidak muncul), memakai auto-wait tanpa intercept; mengamati toast.
- State yang diubah dan dipulihkan: Filter kedua tab (dibersihkan di langkah 3, 6, dan 12), Search dan Sort tab User Action (dibersihkan di langkah 12). Suite serial (`parallel: false`).

## Test Steps

### TC-AC-ACAL-158: Log lama tidak terhapus otomatis

1. Klik icon Filter pada tab Session, pilih rentang `18 Jun 2024` sampai `18 Jun 2024`, klik [Apply]
2. Verifikasi baris `Uji Retensi {runId}-042` (cap `18 Jun 2024`) tampil di tab Session
3. Klik icon Filter, klik [Clear Field], klik [Apply]
4. Klik tab "User Action", klik icon Filter, pilih rentang `18 Jun 2024` sampai `18 Jun 2024`, klik [Apply]
5. Verifikasi baris `Entri Retensi {runId}-042` (cap `18 Jun 2024`) tampil di tab User Action
6. Klik icon Filter, klik [Clear Field], klik [Apply]

### TC-AC-ACAL-159: Volume besar tidak memblokir browsing

7. Untuk setiap baris tabel "Aksi browsing User Action" di Prerequisites, lakukan langkah 8 sampai 11
8. Lakukan aksi pada kolom Aksi
9. Verifikasi tabel memuat dengan loading component biasa
10. Verifikasi tidak ada loading screen penuh
11. Verifikasi toolbar (Search, Filter, Download) tetap dapat dioperasikan selama tabel memuat (tidak ada blokir)
12. Klik icon sort pada header kolom Name hingga netral, klik icon Filter, klik [Clear Field], klik [Apply], lalu klik `(←)` pada kotak Search

### TC-AC-ACAL-171: Download tanpa batas jumlah baris (XLSX dan CSV)

13. Baca Z dari footer tab User Action (`Showing X–Y of Z entries`), klik icon Download, lalu klik `Download as XLSX`
14. Verifikasi loading screen tampil
15. Verifikasi tidak ada toast error
16. Verifikasi berkas `Activity-Log-User-Action.xlsx` terunduh
17. Buka isi berkas yang terunduh
18. Verifikasi sheet `Activity-Log-User-Action` memuat baris header
19. Verifikasi sheet `Activity-Log-User-Action` berisi 1.048.575 baris data (batas baris sheet)
20. Verifikasi sheet `Activity-Log-User-Action-2` memuat baris header yang sama
21. Verifikasi sheet `Activity-Log-User-Action-2` berisi Z − 1.048.575 baris data (sisa dari Z)
22. Klik icon Download, lalu klik `Download as CSV`
23. Verifikasi loading screen tampil
24. Verifikasi berkas `Activity-Log-User-Action.csv` terunduh
25. Buka isi berkas yang terunduh
26. Verifikasi berkas berisi Z baris data (sama dengan Z dari footer pada langkah 13)

## Notes

- Sumber: `admin-console/activity-log/TestCases/tc-activity-log.md`. Urutan TC dalam spec: 158, 159, 171 (kasus kecil lebih dulu, unduhan terberat terakhir). Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE. Kolom Automation ketiga TC bernilai Manual Only di TC (TC-AC-ACAL-159 juga); itu bukan alasan keluar spec, kebutuhan teknisnya ada di Prerequisites.
- Spec ini di atas 35 langkah bila dihitung dengan ekspansi (26 langkah nominal; langkah 8 sampai 11 diulang untuk empat baris tabel Prerequisites sehingga sekitar 38 langkah). Alasan: seluruh blok satu kelas harness (volume data, kelas e) pada satu entitas Volume, dan tiap blok berdiri sendiri: kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah 8 sampai 11 memakai idiom "Untuk setiap baris tabel" tanpa langkah bersyarat; `Verifikasi` tetap satu per klausa.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 3 dan 6 (membersihkan Filter kedua tab, S-09), langkah 12 (membersihkan Sort, Filter, dan Search tab User Action, S-09), langkah 17 dan 25 (membuka isi berkas); langkah 13 menggabungkan pembacaan Z dari footer dengan klik Download (tanpa `Verifikasi`).
- Absence state sementara (bagian 8b butir 11 dan 5): loading screen dan toast diasersi segera setelah pemicu (klik pilihan format) dan sebelum asersi berkas (langkah 14 sampai 16 dan 23 sampai 24); pemicu menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas. Langkah 10 (tidak ada loading screen penuh) memakai langkah 9 (loading component biasa tampil pada tabel yang sama) sebagai anchor positif.
- Z pada langkah 21 dan 26 dibaca dari footer tab User Action pada langkah 13 (bagian 8b butir 10), bukan angka mutlak audit trail hidup; sesuai TC seeding entitas Volume menghasilkan 1.048.577 (sheet kedua 2 baris data), sedangkan batas 1.048.575 baris data per sheet XLSX tetap tertulis di langkah 19; entitas khusus spec menjamin tidak ada baris tambahan dari spec lain, dan entri retensi TC-AC-ACAL-158 sudah dihitung dalam total.
- Label menu Download: TC-AC-ACAL-171 menulis `Download > CSV|XLSX`, label UI adalah `Download as CSV|XLSX` (PRD §4.2); spec memakai label UI.
- Temuan untuk QA:
  - TC-AC-ACAL-158, 159, dan 171 menyebut volume atau entri lama tanpa menyebut akun atau entitas; entitas Volume dan akunnya tidak ada di Pre-setup TC (Pre-setup No 11 hanya menyebut volume seed BE). Mekanisme seed (1.048.577 entri, entri bercap 2024) tidak disebut TC, PRD, atau LLD; disediakan tim FE/BE (S-13).
  - TC-AC-ACAL-158 tidak menyebut jam entri `18 Jun 2024` dan Time Zone; spec memakai jam bebas dan filter satu hari.
  - TC-AC-ACAL-159 tidak menyebut nilai Search, Filter, dan Sort serta tidak mendefinisikan "blokir"; spec memakai nilai dari tabel Prerequisites dan mengasersi blokir sebagai toolbar yang tetap dapat dioperasikan.
  - TC-AC-ACAL-171 menyebut `Activity-Log-User-Action.xlsx` dengan dua sheet (1.048.575 dan 2 baris data) sesuai batas baris XLSX; tidak menyebut apakah kolom lain ikut. Spec hanya mengasersi nama sheet, header, dan jumlah baris data.
  - Post Condition ketiga TC bernilai `-`; tidak diasersi.
