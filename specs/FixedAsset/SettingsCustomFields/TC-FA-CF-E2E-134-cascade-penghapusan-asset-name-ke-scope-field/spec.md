---
id: TC-FA-CF-E2E-134-cascade-penghapusan-asset-name-ke-scope-field
title: "Cascade Penghapusan Asset Name ke Scope Field dan Log"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-503
  - TC-FA-CF-515
  - TC-FA-CF-516
  - TC-FA-CF-517
  - TC-FA-CF-518
  - TC-FA-CF-519
  - TC-FA-CF-520
coverage:
  web: automated
---

# Cascade Penghapusan Asset Name ke Scope Field dan Log

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha, pengguna Sarah Johnson (Modified By `Sarah J`) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Alpha (Pre-setup #1). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Alpha (plan Professional, lisensi FA-7 aktif; Pre-setup #11) dengan baseline tab General delapan field (Pre-setup #12) yang dirujuk lewat fixture `Fixture.faCustomFields.baselineGeneral`. Data Pre-setup #30: Asset Name `Boiler` (tanpa aset terkait, dapat dihapus), field `Boiler Spec` (Scope {Boiler}, Active), `Boiler Pair` (Scope {Boiler, Pump}), dan `Boiler Rating` (Text, Global, Scope {Boiler, Pump}, `Boiler` = `A`, `Pump` = `B`); aset konsumen A1 (Asset Name `Pump`, Active; Pre-setup #31) membuat Asset Name `Pump` in-use. Data dirujuk lewat fixture `Fixture.faCustomFields.boiler`.
- Waktu: jam server dan jam browser sinkron; Last Updated dibandingkan dengan waktu penghapusan yang dicatat sesudah aksi dengan toleransi satu menit (S-12).
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah dan isi entri Changelog tab General, System Log pengguna aktor, dan Activity Log untuk baseline dan perbandingan; total entri tidak diasersi sebagai angka absolut, hanya selisih terhadap baseline (S-12). Seed reset Company untuk memulihkan baseline. Seed reset Company juga memulihkan Asset Name `Boiler`.
- Pemulihan: hook `before` memulihkan baseline Company lewat seed reset Company; hook `after` membersihkan field Dinamis milik spec dan memulihkan baseline (Last Updated dan Modified By field baseline berubah oleh aksi spec; dipulihkan seed reset). Hook `after` memulihkan Asset Name `Boiler` dan ketiga field Boiler.
- State global: tidak ada yang diubah.
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-503: Penghapusan Asset Name mencatat Edit Scope dengan aktor penghapus di tiga surface

1. Pada Modal Changelog tab General, System Log `Sarah Johnson`, dan Activity Log ketik Search `Boiler Pair` (satu per satu) dan catat jumlah baris hasil Search masing-masing sebagai baseline, lalu kembali ke Fixed Asset > Settings > Custom Fields (tab General); catat juga Data Type dan Value Type `Boiler Spec`
2. Hapus Asset Name `Boiler` di Settings > Asset Name oleh Total Control `Sarah Johnson` dan konfirmasi dialog hapus
3. Catat waktu penghapusan (jam server dan jam browser sinkron; toleransi satu menit)
4. Tunggu aksi selesai (dialog hapus tertutup dan daftar Asset Name dimuat ulang)
5. Buka Modal Changelog tab General, ketik Search `Boiler Pair`, tekan Enter
6. Verifikasi Changelog memuat satu baris baru dengan Action `Edit`, Field Name `Boiler Pair`, Field `Scope`, Old Value `Boiler`, New Value `—`, Modified By `Sarah J`
7. Verifikasi hasil Search `Boiler Pair` pada Changelog bertambah tepat satu baris dibanding baseline (tidak ada baris ganda)
8. Verifikasi Changelog tidak memuat baris `Global Value` untuk `Boiler Pair`
9. Buka Settings > User > Detail pengguna `Sarah Johnson` > Tab System Log, ketik Search `Boiler Pair`, tekan Enter
10. Verifikasi System Log `Sarah Johnson` memuat satu baris baru dengan Action `Edit`, Object `Custom Fields`, Name `Boiler Pair`, Field `Scope`, Old Value `Boiler`, New Value `—`
11. Verifikasi hasil Search `Boiler Pair` pada System Log `Sarah Johnson` bertambah tepat satu baris dibanding baseline (tidak ada baris ganda)
12. Buka Reports & Logs > Activity Log > Tab User Action, ketik Search `Boiler Pair`, tekan Enter
13. Verifikasi Activity Log memuat satu baris baru dengan Action `Edit`, Object `Custom Fields`, Name `Boiler Pair`, Field `Scope`, Old Value `Boiler`, New Value `—`, Modified By `Sarah J`
14. Verifikasi hasil Search `Boiler Pair` pada Activity Log bertambah tepat satu baris dibanding baseline (tidak ada baris ganda)

### TC-FA-CF-515: Asset Name satu-satunya anggota Scope dihapus, Scope field menjadi kosong

15. Kembali ke Fixed Asset > Settings > Custom Fields (tab General)
16. Verifikasi kolom Scope baris `Boiler Spec` menampilkan `—`
17. Verifikasi switch Active baris `Boiler Spec` tidak berubah (tetap ON)
18. Verifikasi Data Type dan Value Type baris `Boiler Spec` sama dengan nilai yang dicatat pada langkah 1
19. Verifikasi Last Updated baris `Boiler Spec` sesuai waktu penghapusan yang dicatat pada langkah 3 (toleransi satu menit)
20. Verifikasi Modified By baris `Boiler Spec` menampilkan `Sarah J`

### TC-FA-CF-516: Asset Name salah satu anggota Scope dihapus, himpunan menyusut dan Scope tetap Specific

21. Verifikasi kolom Scope baris `Boiler Pair` menampilkan badge `Pump` saja
22. Verifikasi kolom Scope baris `Boiler Pair` bukan `—` dan bukan `General` (tetap Specific Asset Name)

### TC-FA-CF-517: Nilai Global milik Asset Name yang dihapus dibuang

23. Klik row action `⋯` > `Edit` pada baris `Boiler Rating`
24. Verifikasi Edit menampilkan satu input `Pump` ber-pre-filled `B`
25. Verifikasi nilai Global `Boiler` tidak ada lagi pada Edit
26. Tutup modal Edit dengan `✕` (form belum diubah, sehingga tanpa dialog `Unsaved Changes`)

### TC-FA-CF-519: Field ber-Scope kosong tidak tampil di form aset

27. Buka form registrasi aset pada modul Asset Registration dan pilih Asset Name `Pump`
28. Verifikasi label `Asset Serial Tag` tampil
29. Verifikasi label `Boiler Spec` tidak tampil karena Scope kosong tidak cocok dengan Asset Name mana pun

### TC-FA-CF-520: Asset Name in-use tidak dapat dihapus

30. Catat Scope baris `Equipment Class` di Settings > Custom Fields
31. Coba hapus Asset Name `Pump` di Settings > Asset Name
32. Verifikasi penghapusan ditolak oleh guard in-use dan Asset Name `Pump` masih ada di Settings > Asset Name
33. Kembali ke Settings > Custom Fields dan verifikasi Scope baris `Equipment Class` yang memuat `Pump` tidak berubah

### TC-FA-CF-518: Field ber-Scope kosong tetap dapat di-Activate, di-Deactivate, dan di-Delete

34. Geser switch Active baris `Boiler Spec` ke OFF lalu klik `[Deactivate]`
35. Verifikasi toast `Success, custom field has been deactivated.` tampil
36. Geser switch Active baris `Boiler Spec` ke ON lalu klik `[Activate]`
37. Verifikasi toast `Success, custom field has been activated.` tampil
38. Klik row action `⋯` > `Delete` pada baris `Boiler Spec`, lalu klik `[Delete]` pada dialog
39. Verifikasi toast `Success, custom field has been deleted.` tampil

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di spec: 503, 515, 516, 517, 519, 520, 518. Asset Name `Boiler` dihapus satu kali (langkah 2) karena TC-FA-CF-503, 515, 516, 517, 518, dan 519 memiliki precondition dan aksi pemicu yang sama ("Hapus Asset Name Boiler"); observasi tiap TC memakai hasil penghapusan itu. TC-FA-CF-518 mengakhiri spec karena Delete `Boiler Spec` menghapus data (S-10); TC-FA-CF-520 tidak bergantung pada penghapusan `Boiler`.
- Alasan di atas 35 langkah: spec memuat 39 langkah bernomor; langkah blok baca-log berpola (buka surface, cari `Boiler Pair`, `Verifikasi` kolom log dan selisih jumlah per surface; 10 langkah, nomor 5 sampai 14) tidak dihitung pada smell (bagian 3), sehingga hitungan efektif 29 langkah. Seluruhnya satu topik (cascade penghapusan Asset Name `Boiler` ke field ber-Scope) dan satu dataset milik spec.
- TC-FA-CF-503 (langkah 1 dan 5 sampai 14): "baris baru" ditulis sebagai selisih satu baris pada jumlah baris hasil Search `Boiler Pair` terhadap baseline per surface, karena nama field tidak unik pada audit trail permanen (S-12).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (baseline jumlah baris hasil Search `Boiler Pair` per surface dan pencatatan Data Type, Value Type `Boiler Spec`), langkah 3 (mencatat waktu), langkah 4 ("Tunggu aksi selesai" sesudah penghapusan Asset Name sebelum Modal Changelog dibuka; 8b butir 8; asersi tambahan di luar Expected TC, S-03), langkah buka surface serta temukan baris (R-16), kembali ke Settings > Custom Fields, dan penutupan modal Edit tanpa perubahan.
- Temuan untuk QA:
  - TC-FA-CF-503 Expected a menulis Old Value `Boiler` dan New Value `—` pada `Boiler Pair` yang ber-Scope {Boiler, Pump}; TC-FA-CF-516 menyatakan Scope `Boiler Pair` menyusut menjadi `Pump`. Old Value `Boiler`/New Value `—` konsisten dengan `Boiler Spec` (Scope {Boiler}), bukan `Boiler Pair`; spec mengikuti TC apa adanya.
  - TC-FA-CF-503 menghapus Asset Name, yang juga mengubah `Boiler Spec` dan `Boiler Rating`; TC tidak menyebut baris log untuk kedua field itu sehingga jumlah entri total tidak diasersi.
  - TC-FA-CF-515 Expected b menyebut "Data Type, Value Type, dan konfigurasi lain dipertahankan" tanpa nilai konkret; spec membandingkan Data Type dan Value Type dengan nilai yang dicatat sebelum penghapusan.
  - TC-FA-CF-518 tidak menyebut teks toast; spec memakai teks toast baku `Success, custom field has been deactivated.`, `Success, custom field has been activated.`, dan `Success, custom field has been deleted.` dari TC Toggle dan Delete.
  - TC-FA-CF-519 melintasi modul Asset Registration (NC-01); spec hanya mengasersi label field sejauh teks Expected TC.
  - TC-FA-CF-520 tidak menyebut teks penolakan guard in-use; spec mengasersi penolakan dan Asset Name tetap ada tanpa teks pesan.
  - Email akun Total Control Company Alpha mengikuti pola Pre-setup #1; env var `FA_TC_PASSWORD` disediakan tim FE.
