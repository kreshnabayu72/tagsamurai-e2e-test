---
id: TC-AC-DN-E2E-102-search-karakter-khusus-last-modified-kolom-tersembunyi
title: "Search List: Karakter Khusus, Last Modified Tidak Dicari, Kolom Tersembunyi, dan Reset Halaman"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DN-283
  - TC-AC-DN-284
  - TC-AC-DN-285
  - TC-AC-DN-286
  - TC-AC-DN-287
coverage:
  web: automated
---

# Search List: Karakter Khusus, Last Modified Tidak Dicari, Kolom Tersembunyi, dan Reset Halaman

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (`suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Data Pre-setup (hanya dibaca, tidak diubah): #16 Device Name inti (`Cable Tester`, `Tag Reel` ber-Measurement `Meter`), #17 seed `Seed Device 001` sampai `Seed Device 120`, #19 riwayat Changelog (Last Modified `Cable Tester` 10/09/26 12:25), dan #20 General Settings (Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Tidak ada data Dinamis dan tidak ada aksi tulis.
- Nilai data dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE).
- State global: konfigurasi Column Visibility (kolom Measurement) disimpan di browser. Spec mengembalikannya lewat langkah eksplisit; hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE). Kotak Search dikosongkan di akhir spec. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-283: Karakter khusus dan markup dicocokkan sebagai teks biasa

1. Ketik Search `<script>alert(1)</script>`, tekan Enter
2. Verifikasi empty state Title "No results found" dan Description "Try adjusting your search or filter."
3. Verifikasi tidak ada dialog atau skrip yang berjalan
4. Ganti isi kotak search dengan `%`, tekan Enter
5. Verifikasi empty state Title "No results found" dan Description "Try adjusting your search or filter." (tidak dibaca sebagai wildcard)
6. Ganti isi kotak search dengan `.*`, tekan Enter
7. Verifikasi empty state Title "No results found" dan Description "Try adjusting your search or filter." (tidak dibaca sebagai pola)

### TC-AC-DN-284: Nilai Last Modified tidak dapat dicari lewat kotak Search

8. Ganti isi kotak search dengan `10/09/26`, tekan Enter
9. Verifikasi empty state Title "No results found" dan Description "Try adjusting your search or filter." walau Cable Tester memiliki Last Modified 10/09/26 12:25
10. Klik ikon Filter
11. Verifikasi field `Last Modified` tampil di Filter Panel (penyaringan tanggal hanya tersedia lewat field itu)
12. Klik ikon Filter lagi

### TC-AC-DN-285: Kolom Measurement yang disembunyikan tidak ikut dicari

13. Klik `(←)` pada kotak Search
14. Klik header kolom Actions `⋯`, hapus centang `Measurement`
15. Ketik Search `Meter`, tekan Enter
16. Verifikasi empty state Title "No results found" dan Description "Try adjusting your search or filter." karena kolom Measurement sedang disembunyikan

### TC-AC-DN-286: Kolom Measurement yang ditampilkan kembali ikut dicari

17. Klik `(←)` pada kotak Search
18. Klik header kolom Actions `⋯`, centang `Measurement` kembali
19. Klik header kolom Actions `⋯`, hapus centang `Measurement` lalu centang `Measurement` kembali
20. Ketik Search `Meter`, tekan Enter
21. Verifikasi tabel menampilkan 1 baris: Tag Reel (Measurement `Meter`)

### TC-AC-DN-287: Search dari halaman lebih dari 1 kembali ke halaman 1

22. Klik `(←)` pada kotak Search
23. Klik tombol halaman berikutnya
24. Ketik Search `Seed Device`, tekan Enter
25. Verifikasi hasil pencarian tampil mulai halaman 1 (Seed Device 001 sampai Seed Device 010), bukan halaman 2
26. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini tanpa aksi tulis.
- Langkah penghubung (S-03, S-09): langkah 10 dan 12 membuka dan menutup Filter Panel untuk TC-AC-DN-284; langkah 13, 17, 22, dan 26 mengosongkan Search; langkah 18 memulihkan kolom Measurement yang disembunyikan di langkah 14 sebelum TC-AC-DN-286 mengulang hide dan show.
- Urutan: mengikuti sourceTc; Search kosong hasil (TC-AC-DN-283 dan TC-AC-DN-284) di awal, lalu Column Visibility, lalu reset halaman.
- Temuan untuk QA:
  - TC-AC-DN-284 Expected b ("penyaringan tanggal hanya tersedia lewat field `Last Modified` di Filter Panel") tidak punya langkah observasi di TC; spec mengasersinya lewat tampilnya field `Last Modified` di Filter Panel (langkah 11).
  - TC-AC-DN-285 dan TC-AC-DN-286: langkah hide pada TC kedua tidak mencantumkan bahwa kolom Measurement dipulihkan di antara keduanya; spec memulihkannya di langkah 18.
