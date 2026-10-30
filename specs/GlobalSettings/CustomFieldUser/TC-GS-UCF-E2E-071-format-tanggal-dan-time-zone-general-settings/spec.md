---
id: TC-GS-UCF-E2E-071-format-tanggal-dan-time-zone-general-settings
title: "Format Tanggal dan Waktu General Settings pada Last Updated, Filter, Modal Changelog, Time Zone, dan Berkas Download CSV"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-292
  - TC-GS-UCF-293
  - TC-GS-UCF-413
  - TC-GS-UCF-414
  - TC-GS-UCF-415
  - TC-GS-UCF-416
coverage:
  web: automated
---

# Format Tanggal dan Waktu General Settings pada Last Updated, Filter, Modal Changelog, Time Zone, dan Berkas Download CSV

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec ini mengubah state global Client A (Date Format, Time Format, Time Zone di General Settings) yang memengaruhi tampilan tanggal spec lain; tidak boleh dijalankan paralel dengan spec lain di Client A.
- Akun aktor: Total Control Client A Sari Dewi (Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field; langkah yang membuka ulang halaman itu berfungsi sebagai pemulihan state sesudah perubahan General Settings atau Search.
- Data Pre-setup (baca-saja, tidak diubah spec ini): 6 Custom Field Pre-setup Client A (Last Updated: `Cost Center` 11 Sep 2026 10:35, `Employee Grade` 10 Sep 2026 14:15, `Job Description` 10 Sep 2026 11:00, `Bonus` 9 Sep 2026 15:20, `Office Phone` 9 Sep 2026 10:10, `Joining Date` 9 Sep 2026 09:00; fixture backend) dan Changelog Pre-setup 8 entri bertanggal 8 sampai 11 Sep 2026 (termasuk Create `Job Description` oleh Siti R). Data Population (8 Custom Field, 8 entri Create) dibuat lewat API oleh Sari Dewi di hook `before` bila belum ada (seeding idempotent); dipakai sebagai precondition TC (total 14 Custom Field), tidak diasersi satu per satu.
- State global General Settings Client A yang diatur spec ini (nilai awal: Date Format `DDD, MMM dd, yyyy`, Time Format `hh:mm a`, Time Zone berlabel `(UTC+07:00)` dengan nilai tersimpan `Asia/Jakarta`):
  - TC-GS-UCF-292 dan 293: Date Format `DDD, MMM dd, yyyy`, Time Format `hh:mm a` (nilai awal).
  - TC-GS-UCF-413, 414, dan 415: Date Format `dd MMM yy`, Time Format `HH:mm`; Time Zone `(UTC+07:00)` awalnya, lalu `(UTC+08:00)` pada TC-GS-UCF-415 dan dipulihkan ke `(UTC+07:00)` pada langkah terakhir TC itu.
  - TC-GS-UCF-416: Date Format `M/d/yy`, Time Format `HH:mm`.
  - Pengubah Date Format dan Time Format di General Settings Client A disediakan tim FE/BE (mekanisme tidak ada di TC, PRD modul ini, atau LLD); Time Zone diubah lewat UI General Settings sesuai langkah TC-GS-UCF-415. Hook `after` memulihkan ketiganya ke nilai awal walau spec gagal di tengah.
- Jam server dan jam browser sinkron; bagian Date dan jam Last Updated Pre-setup berasal dari fixture backend dan tidak bergantung pada jam nyata.
- Setup Column Modal Changelog dan tabel utama: konfigurasi default; hook `beforeEach` membersihkan cache browser.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_<page_key>` true untuk akun aktor dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: date picker pada Filter Last Updated (tabel utama) dan Filter Date (Modal Changelog); pembaca berkas CSV (TC-GS-UCF-416); halaman Global Settings > General Settings.
- State global lain: tidak ada selain flag Guided Tooltip.

## Test Steps

### Format default: DDD, MMM dd, yyyy dan hh:mm a (TC-GS-UCF-292 dan 293)

1. Atur General Settings Client A: Date Format `DDD, MMM dd, yyyy`, Time Format `hh:mm a` (nilai awal, disediakan tim FE/BE)
2. Buka Global Settings > User > Custom Field

### TC-GS-UCF-292: Date dan Time Format pada kolom Last Updated tabel utama dan input filter

3. Verifikasi kolom Last Updated berpola `DDD, MMM dd, yyyy hh:mm a`
4. Klik Filter, pilih tanggal di Last Updated
5. Verifikasi input filter Last Updated menampilkan `DDD, MMM dd, yyyy`
6. Klik `[Clear Field]`, lalu tutup panel Filter

### TC-GS-UCF-293: Date dan Time Format pada Modal Changelog

7. Klik icon Changelog
8. Verifikasi kolom Date berpola `DDD, MMM dd, yyyy hh:mm a`
9. Klik Filter, pilih tanggal di Date
10. Verifikasi input filter Date menampilkan `DDD, MMM dd, yyyy`
11. Klik `[Clear Field]`, lalu klik `[✕]`

### Format dd MMM yy dan HH:mm (TC-GS-UCF-413, 414, dan 415)

12. Atur General Settings Client A: Date Format `dd MMM yy`, Time Format `HH:mm` (disediakan tim FE/BE)
13. Buka Global Settings > User > Custom Field

### TC-GS-UCF-413: Format dd MMM yy dan HH:mm pada kolom Last Updated tabel utama dan input filter

14. Verifikasi kolom Last Updated berpola `dd MMM yy HH:mm`
15. Verifikasi jam Last Updated memakai 24 jam tanpa AM/PM
16. Klik Filter, pilih tanggal di Last Updated
17. Verifikasi input filter Last Updated menampilkan `dd MMM yy`
18. Klik `[Clear Field]`, lalu tutup panel Filter

### TC-GS-UCF-414: Format dd MMM yy dan HH:mm pada Modal Changelog

19. Klik icon Changelog
20. Verifikasi kolom Date berpola `dd MMM yy HH:mm`
21. Verifikasi jam Date memakai 24 jam tanpa AM/PM
22. Klik Filter, pilih tanggal di Date
23. Verifikasi input filter Date menampilkan `dd MMM yy`
24. Klik `[Clear Field]`, lalu klik `[✕]`

### TC-GS-UCF-415: Perubahan Time Zone menggeser jam Last Updated dan Date Changelog

25. Ketik Search `Job Description` pada tabel utama, tekan Enter
26. Catat jam Last Updated baris `Job Description` (T1)
27. Klik icon Changelog
28. Ketik Search `Job Description`, tekan Enter
29. Catat Date entri Create `Job Description` (T2)
30. Klik `[✕]`
31. Buka Global Settings > General Settings
32. Pilih Time Zone berlabel `(UTC+08:00)`
33. Klik `[Save]`
34. Tunggu aksi selesai
35. Buka Global Settings > User > Custom Field
36. Ketik Search `Job Description` pada tabel utama, tekan Enter
37. Verifikasi tanggal Last Updated baris `Job Description` sama dengan T1
38. Verifikasi jam Last Updated baris `Job Description` satu jam setelah T1
39. Klik icon Changelog
40. Ketik Search `Job Description`, tekan Enter
41. Verifikasi tanggal Date entri Create `Job Description` sama dengan T2
42. Verifikasi jam Date entri Create `Job Description` satu jam setelah T2
43. Klik `[✕]`
44. Buka Global Settings > General Settings
45. Pilih kembali Time Zone berlabel `(UTC+07:00)`
46. Klik `[Save]`
47. Tunggu aksi selesai
48. Buka Global Settings > User > Custom Field

### Format M/d/yy dan HH:mm (TC-GS-UCF-416)

49. Atur General Settings Client A: Date Format `M/d/yy`, Time Format `HH:mm` (disediakan tim FE/BE)
50. Buka Global Settings > User > Custom Field

### TC-GS-UCF-416: Download CSV memakai Date Format dan Time Format yang sama dengan List

51. Ketik Search `Cost Center` pada tabel utama, tekan Enter
52. Verifikasi kolom Last Updated baris `Cost Center` pada tabel berpola `M/d/yy HH:mm`
53. Catat nilai Last Updated baris `Cost Center` pada tabel (T3)
54. Klik Download > `Download as CSV`
55. Buka berkas CSV
56. Verifikasi kolom Last Updated baris `Cost Center` pada berkas berpola `M/d/yy HH:mm`
57. Verifikasi nilai Last Updated baris `Cost Center` pada berkas sama dengan T3
58. Atur General Settings Client A kembali ke Date Format `DDD, MMM dd, yyyy`, Time Format `hh:mm a` (pemulihan state, disediakan tim FE/BE)

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Spec melewati sekitar 35 langkah (smell, bagian 3 prinsip 13 konvensi): 6 TC satu topik (format tanggal dan Time Zone General Settings) dengan satu akun; setiap Expected bermajemuk dipecah satu `Verifikasi` per klausa (S-01) dan blok per TC tetap bermakna bila blok sebelumnya gagal.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah; subjudul tanpa id TC (`Format default`, `Format dd MMM yy dan HH:mm`, `Format M/d/yy dan HH:mm`) memuat langkah penghubung yang mengatur General Settings.
- Urutan TC dalam spec: 292, 293, 413, 414, 415, 416. Urutan mengelompokkan TC menurut format yang berlaku supaya pengaturan General Settings tidak diulang per TC (TC-GS-UCF-413, 414, dan 415 berbagi Date Format `dd MMM yy` dan Time Format `HH:mm`). TC-GS-UCF-415 memakai Time Format `HH:mm` dari precondition dan melanjutkan Date Format `dd MMM yy` dari TC-GS-UCF-414 karena precondition TC hanya menyebut Time Zone dan Time Format.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah mengatur General Settings, pembukaan ulang Global Settings > User > Custom Field, `[Clear Field]` dan penutupan panel Filter sesudah memilih tanggal (tanpa `[Apply]`, supaya TC berikutnya mulai tanpa filter), `[✕]` pada Modal Changelog (tanpa dialog karena tidak ada form), Search `Job Description` dan `Cost Center` untuk menemukan baris, pencatatan T1, T2, dan T3, dan langkah "Tunggu aksi selesai" sesudah `[Save]` General Settings yang berpindah surface (bagian 8b butir 8). Pemulihan state global ke nilai awal ditulis sebagai langkah eksplisit di akhir spec dan di hook `after`.
- TC-GS-UCF-416 memakai Search `Cost Center` untuk menemukan baris `Cost Center` pada halaman tabel; Download kemudian mengikuti Search aktif, sehingga berkas memuat baris yang cocok dengan Search `Cost Center`.
- Spec berjumlah 58 langkah, di atas ambang sekitar 35. Seluruhnya satu kelas h (format tanggal General Settings, state global) yang satu permukaan: tabel utama, Modal Changelog, dan berkas export. Tiap blok TC berdiri sendiri, dimulai dari pengaturan format sendiri, dan state global dipulihkan di akhir dan di hook `after`.
- Topik satu permukaan lain (format tanggal pada Download Changelog) tidak diasersi di spec ini; TC-GS-UCF-530 (spec 066) mengasersi Date berkas Changelog dalam Date Format default.
- Temuan untuk QA:
  - TC-GS-UCF-292, 293, 413, 414, dan 416 memakai kata "berpola" dan tidak memuat contoh nilai; spec mengasersi pola format, bukan nilai literal tanggal.
  - TC-GS-UCF-413 dan 414 menyebut Time Format `HH:mm` sebagai "24 jam"; nilai "24 jam" bertanda `PRD?` di TC. Spec mengasersi 24 jam tanpa AM/PM sesuai Expected TC.
  - TC-GS-UCF-415 tidak menyebut Date Format yang berlaku; spec memakai `dd MMM yy` (nilai berurutan dari TC-GS-UCF-414). Time Zone `(UTC+07:00)` dan nilai tersimpan `Asia/Jakarta` adalah precondition TC dan dipulihkan pada langkah terakhir.
  - TC-GS-UCF-415: Last Updated dan Date Changelog Pre-setup berasal dari fixture backend; jika fixture memakai zona waktu berbeda dari `(UTC+07:00)`, selisih "satu jam" tetap berlaku karena diasersi relatif terhadap catatan sebelum perubahan.
  - TC-GS-UCF-416 langkah 1 menyebut "baris Cost Center pada tabel" tanpa menyebut halaman tempat baris tampil; spec memakai Search `Cost Center`.
  - Pengubah Date Format dan Time Format General Settings: tidak ada langkah UI di TC (hanya precondition); mekanisme "disediakan tim FE/BE" dan, bila tersedia, UI General Settings.
