---
id: TC-GS-UCF-E2E-059-multi-konteks-list-tidak-otomatis-dan-filter-basi
title: "Multi-Konteks Tabel Custom Field: Kriteria Filter Basi karena Record Dihapus Sesi Lain dan List Tidak Diperbarui Otomatis"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-UCF-355
  - TC-GS-UCF-556
coverage:
  web: automated
---

# Multi-Konteks Tabel Custom Field: Kriteria Filter Basi karena Record Dihapus Sesi Lain dan List Tidak Diperbarui Otomatis

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor sesi A: Total Control Client A (Sari Dewi, Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net`. Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Pelaku sesi B (admin kedua Client A, Nadia Pratama, Modified By `Nadia P`) `totalControlSecond_automated_qaTeam1@qwertysystem.net` dengan `Spectra.env.GS_TC2_PASSWORD`: sesi API yang hanya memicu perubahan state (menghapus `Nadia Probe {runId}-059` dan membuat `List Static Probe {runId}-059`) dan hasilnya tidak diasersi di sesi B; langkah pemicu ditulis "hingga ... tersimpan" (P-2). Mekanisme sesi API Admin B disediakan tim FE/BE (endpoint tidak ditulis di spec).
- Data Pre-setup Client A (tetap di environment, tidak diubah spec ini, tanpa suffix; fixture baru (belum ada; lihat coverage) `Fixture.customFieldUser.preset14`): 6 Custom Field `Cost Center`, `Employee Grade`, `Job Description`, `Bonus`, `Office Phone`, dan `Joining Date`; dipakai sebagai precondition TC (total 14 field), tidak diasersi.
- Data Dinamis Population D-01 (8 field; fixture baru (belum ada; lihat coverage) `Fixture.customFieldUser.population`): `Blood Type`, `Shirt Size`, `Emergency Phone`, `Birth Date`, `Tax ID`, `Work Notes`, `Annual Target`, `badge number`; Active; Modified By `Sari D`. Di-seed lewat API oleh akun Total Control Client A di hook `before` (mekanisme disediakan tim FE/BE); dipakai sebagai precondition TC, tidak diasersi. Nama literal tanpa suffix (pengecualian Population, S-12); seeding idempotent (dilewati bila sudah ada); cleanup hanya menghapus yang dibuat hook spec ini.
- Data Dinamis milik spec (nama bersuffix per run; fixture baru `Fixture.customFieldUser.multiContext059`): `Nadia Probe {runId}-059` (D-134: Text; dibuat dan satu-satunya diubah oleh Nadia Pratama, Modified By `Nadia P`) di-seed lewat sesi API Admin B di hook `before` dan dihapus oleh langkah pemicu TC-GS-UCF-355; `List Static Probe {runId}-059` (D-247: Text) dibuat oleh sesi B pada langkah TC-GS-UCF-556 dan belum ada saat sesi A membuka tab.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field; spec tidak menguji navigasi sehingga tidak mengulang langkah buka di `## Test Steps`.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Nadia Probe {runId}-059` bila masih ada, `List Static Probe {runId}-059`, dan field Population yang dibuat hook `before`; kosongkan Search dan Filter sesi A.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_<page_key>` halaman Custom Field true untuk akun aktor sesi A dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: sesi API kedua untuk Admin B; menunggu jeda nyata 10 detik tanpa memuat ulang halaman (TC-GS-UCF-556, nilai 10 detik dari TC; jeda pendek yang disebut eksplisit di sini, bagian 6 konvensi); pembacaan opsi dropdown Filter dan kondisi tabel tanpa error atau crash.
- State global: tidak ada yang diubah selain data milik spec.

## Test Steps

### TC-GS-UCF-355: Kriteria filter yang menjadi basi karena record dihapus sesi lain

1. Klik Filter
2. Buka dropdown Modified By, pilih `Nadia P`, klik [Apply]
3. Verifikasi tabel menampilkan baris `Nadia Probe {runId}-059`
4. Klik icon Filter untuk menutup panel
5. Sesi B (API) menghapus `Nadia Probe {runId}-059` hingga tersimpan
6. Pada sesi A klik Filter
7. Klik [Apply] kembali
8. Verifikasi halaman Custom Field tetap termuat tanpa error dan tanpa crash
9. Verifikasi baris `Nadia Probe {runId}-059` tidak tampil di tabel
10. Klik [Clear Field], klik [Apply], lalu klik icon Filter untuk menutup panel

### TC-GS-UCF-556: List tidak diperbarui otomatis oleh perubahan admin lain dan diperbarui saat tab dibuka

11. Pada sesi A ketik Search `List Static Probe {runId}-059`, tekan Enter
12. Verifikasi Illustration tampil
13. Verifikasi Title "No results found"
14. Verifikasi Description "Try adjusting your search or filter."
15. Sesi B (API) membuat field `List Static Probe {runId}-059` (Text) hingga tersimpan
16. Sesi A memperhatikan tabel tanpa memuat ulang halaman selama 10 detik
17. Verifikasi tabel sesi A tetap menampilkan Illustration "No results found"
18. Verifikasi baris `List Static Probe {runId}-059` tidak tampil di tabel sesi A
19. Pada sesi A klik tab `Position`, lalu klik tab `Custom Field`
20. Ketik Search `List Static Probe {runId}-059`, tekan Enter
21. Verifikasi tabel sesi A memuat baris `List Static Probe {runId}-059`
22. Klik `(←)`

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Kelas c (multi-konteks): dua sesi (sesi A UI, sesi B API sebagai pemicu). Sesi B hanya memicu perubahan state dan hasilnya tidak diasersi di sesi B, sehingga memakai sesi API, bukan sesi UI kedua (bagian 3 prinsip 13, P-2).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 4 dan 10 (menutup Filter Panel dan mengosongkan Filter), langkah 5 dan 15 (pemicu sesi B), langkah 16 (jeda 10 detik tanpa muat ulang halaman, aksi pengamatan yang kemudian diasersi pada langkah 17 dan 18), langkah 19 (pindah tab), dan langkah 22 (`(←)` menutup input Search).
- Verifikasi tambahan di luar Expected TC (S-03): langkah 3 (baris `Nadia Probe {runId}-059` tampil sesudah Apply pertama) sebagai anchor positif sebelum kriteria filter menjadi basi; Expected TC-GS-UCF-355 hanya menyebut langkah 3 setelah Apply ulang.
- Asersi absence: langkah 9 beranchor pada langkah 8 (halaman tetap termuat, tanpa error dan tanpa crash; tidak ada baris pembanding karena filter Modified By `Nadia P` hanya cocok dengan field itu). Langkah 18 beranchor pada Illustration "No results found" langkah 17 (empty state Search yang diproses adalah anchor positif yang sah).
- Pembagian TC lintas spec: Filter Panel tabel utama (TC-GS-UCF-201 sampai 213, 221, 351 sampai 354, 397) ada di spec 052.
- Temuan untuk QA:
  - TC-GS-UCF-355 Expected tidak menyebut tampilan tabel setelah Apply ulang (kemungkinan empty state "No results found") dan tidak menyebut status opsi `Nadia P` di dropdown Modified By setelah field dihapus; spec hanya mengasersi dua Expected TC (tanpa error dan crash, baris tidak tampil).
  - TC-GS-UCF-355 langkah 2 menulis "Sesi B menghapus Nadia Probe" tanpa menyebut mekanisme; spec memakai sesi API Admin B (P-2, bagian 3 konvensi). Tabel Pre-setup TC menyebut Admin B `totalControlSecond_automated_qaTeam1@qwertysystem.net` (Nadia Pratama).
  - TC-GS-UCF-556 menandai Data Uji "10 detik" sebagai nilai yang tidak ditemukan verbatim di PRD (`PRD?`); spec mengikuti nilai TC.
  - TC-GS-UCF-556 langkah 5 menulis Search ulang tanpa menyebut apakah kotak Search masih terisi sesudah pindah tab; spec memakai langkah atomik "Ketik Search ..., tekan Enter" (bagian 8b butir 9).
  - TC-GS-UCF-355 dan TC-GS-UCF-556 Post Condition: TC-GS-UCF-556 mencatat `List Static Probe (D-247)`; tidak ada langkah observasi, tidak diasersi.
