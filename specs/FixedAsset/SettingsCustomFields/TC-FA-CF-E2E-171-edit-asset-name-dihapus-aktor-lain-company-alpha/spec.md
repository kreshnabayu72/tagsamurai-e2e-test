---
id: TC-FA-CF-E2E-171-edit-asset-name-dihapus-aktor-lain-company-alpha
title: "Edit: Asset Name pada Scope Dihapus Aktor Lain Saat Modal Terbuka"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CF-608
coverage:
  web: automated
---

# Edit: Asset Name pada Scope Dihapus Aktor Lain Saat Modal Terbuka

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor UI sesi 1: Total Control Company Alpha `totalControl_automated_{namaCompany}@qwertysystem.net` (pengguna Sarah Johnson, Pre-setup #1). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Akun pelaku sesi 2 (Pre-setup #10 dan #28): Total Control sesi 2 Company Alpha `totalControlSecond_automated_{namaCompany}@qwertysystem.net` (pengguna Rina Putri). Dipakai dua cara: sesi API (login API dengan `Spectra.env.FA_TC2_PASSWORD`, token tidak dihitung sebagai sesi web) untuk menghapus Asset Name, dan login UI sesudah semua aksi untuk membaca System Log `Rina Putri` (ganti akun eksplisit pada langkah bersangkutan).
- Data Pre-setup Company Alpha (#11 dan #12; 8 field tab General pada halaman pertama): dipakai `Storage Capacity` (Numeric 0 Decimal Places, Scope {Generator, Pump}) dan Asset Name `Pump`. Spec memakai baseline #11 yang tidak memuat aset konsumen, sehingga seluruh Asset Name #11 tidak in-use dan `Pump` dapat dihapus sesi 2; varian dengan aset konsumen (Pre-setup #31: A1 `Pump`, A2 `Generator`) tidak dipakai spec ini. Nama hasil edit Dinamis bersuffix `Storage Capacity Edit {runId}-171`. Nilai data mengacu `Fixture.faCustomFields.alpha` (fixture baru, disediakan tim FE).
- Kemampuan teknis: membaca jumlah dan isi entri Changelog tab General, Activity Log, dan System Log per aktor (disediakan tim FE/BE); sesi API untuk menghapus Asset Name.
- Waktu: jam server dan jam browser sinkron; Date entri log dibandingkan dengan waktu yang dicatat sesudah penghapusan oleh sesi API dengan toleransi satu menit (S-12).
- Baseline: hook `before` memulihkan baseline Company Alpha lewat seed reset Company; hook `after` menyeed ulang Asset Name `Pump` beserta Scope `Storage Capacity` dan field lain yang bercakupan `Pump`, mengembalikan sesi UI ke akun default suite (Total Control Company Alpha), dan membersihkan data Dinamis milik spec. Mekanisme seed disediakan tim FE/BE.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel oleh hook `before` dan `after` suite untuk akun sesi 1 dan sesi 2; lihat `suite.md`.
- State global: Asset Name `Pump` dihapus (dipulihkan hook `after`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-608: Asset Name dihapus saat modal Edit terbuka: Save ditolak dengan pesan stale inline

1. Catat jumlah entri System Log `Sarah Johnson` sebagai baseline sebelum Save
2. Klik row action `⋯` > `Edit` pada baris `Storage Capacity`
3. Sesi API (Rina Putri) menghapus Asset Name `Pump` hingga penghapusan tersimpan
4. Catat waktu sesudah sesi API menyimpan
5. Ubah Field Name menjadi `Storage Capacity Edit {runId}-171`
6. Klik `[Save]`
7. Verifikasi pesan inline `Pump no longer exists. Please select another.` tampil pada input Asset Name
8. Verifikasi chip `Pump` dihapus dari input Scope
9. Verifikasi modal tetap terbuka
10. Verifikasi input lain dipertahankan: Field Name masih `Storage Capacity Edit {runId}-171`
11. Klik icon close `[✕]`
12. Verifikasi dialog `Unsaved Changes` tampil
13. Klik `[Leave]`
14. Verifikasi Field Name baris di tabel tetap `Storage Capacity` (tidak ada mutasi dari Save sesi 1)
15. Buka Modal Changelog tab General, ketik Search `Storage Capacity`, tekan Enter
16. Verifikasi Changelog memuat entri Edit properti `Scope` untuk `Storage Capacity` akibat penghapusan Asset Name `Pump` oleh sesi 2 dengan Date sesuai waktu yang dicatat (toleransi satu menit)
17. Verifikasi Changelog tidak memuat entri Edit properti `Field Name` dengan nilai baru `Storage Capacity Edit {runId}-171` dari Save sesi 1
18. Buka Activity Log (Reports & Logs > Activity Log > Tab User Action), ketik Search `Storage Capacity`, tekan Enter
19. Verifikasi Activity Log memuat entri Edit properti `Scope` untuk `Storage Capacity` akibat penghapusan Asset Name `Pump` oleh sesi 2
20. Verifikasi Activity Log tidak memuat entri dengan nilai baru `Storage Capacity Edit {runId}-171` dari Save sesi 1
21. Buka System Log `Sarah Johnson` (sesi 1) dan hitung ulang jumlah entri
22. Verifikasi jumlah entri System Log `Sarah Johnson` sama dengan jumlah yang dicatat pada langkah 1 (tidak bertambah entri baru dibanding sebelum Save)
23. Ganti akun: `Logout` dari Total Control Company Alpha (Sarah Johnson)
24. Login sebagai Total Control sesi 2 Company Alpha (Rina Putri) dengan `Spectra.env.FA_TC2_PASSWORD`
25. Buka System Log `Rina Putri`
26. Verifikasi System Log `Rina Putri` memuat entri Edit properti `Scope` untuk `Storage Capacity` akibat penghapusan Asset Name `Pump` dengan Date sesuai waktu yang dicatat (toleransi satu menit)
27. `Logout` dari Total Control sesi 2 Company Alpha (Rina Putri)

## Notes

- Pelaku sesi 2 memicu perubahan state lewat sesi API (bukan konteks kedua kelas c); hasilnya diasersi di sesi UI pertama dan di sesi UI kedua (log). Langkah 3 ditulis "... hingga ... tersimpan" (R-20).
- P-1: klausa "tidak ada entri dari Save sesi 1" TC-FA-CF-608 butir c (langkah 17, 20, dan 22) menempel pada state konflik yang dibangun alur ini (Asset Name `Pump` dihapus sesi 2 saat modal Edit sesi 1 terbuka) dan diasersi dengan nilai baru bersuffix unik `Storage Capacity Edit {runId}-171` serta baseline jumlah entri System Log (S-12, langkah 1); tidak ada spec absence yang memuat aksi nyata untuk TC ini (S-05). Anchor positif (8b butir 2): pesan inline stale (langkah 7) dan entri Edit properti `Scope` dari sesi 2 pada surface yang sama (langkah 16, 19, 26).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (baseline jumlah entri System Log `Sarah Johnson`), langkah 4 (mencatat waktu untuk asersi Date), langkah 11 sampai 13 (menutup form dirty; `Verifikasi` dialog `Unsaved Changes` mengikuti S-08), langkah 15, 18, 21, dan 25 (membuka satu surface log per langkah; Search `Storage Capacity` pada langkah 15 dan 18 menemukan baris target, R-16), langkah 23, 24, dan 27 (ganti akun eksplisit ke sesi 2 untuk membaca System Log `Rina Putri`, lalu logout; hook `after` mengembalikan sesi ke akun default suite).
- Spec ini bukan konteks UI ganda yang berjalan bersamaan: sesi 2 dipakai berurutan setelah semua aksi UI sesi 1, sehingga satu akun web aktif pada satu waktu.
- Penghapusan Asset Name `Pump` juga mempengaruhi field lain yang bercakupan `Pump` (mis. `Equipment Class`); asersi log dibatasi pada entri `Storage Capacity` supaya tidak bergantung pada jumlah entri total (S-12).
- Pre-setup #11 tanpa aset konsumen membuat `Pump` tidak in-use; Pre-setup #31 (A1 `Pump`) adalah varian lain yang tidak dipakai TC-FA-CF-608 maupun spec ini.
- Temuan untuk QA:
  - TC-FA-CF-608 tidak menyebut mekanisme "sesi 2"; spec memakai sesi API untuk menghapus Asset Name.
  - Expected c TC-FA-CF-608 menyebut "tidak ada mutasi dan tidak ada entri dari Save sesi 1" tanpa menyebut cara memeriksa; spec mengasersi lewat Field Name di tabel dan ketiadaan entri bernilai baru `Storage Capacity Edit {runId}-171` di Changelog dan Activity Log, serta jumlah entri System Log `Sarah Johnson` yang tidak bertambah.
  - Cara membuka System Log aktor, System Log `Rina Putri`, dan Activity Log tidak dijelaskan di TC (menu atau jalur navigasi); spec menulisnya persis seperti TC.
