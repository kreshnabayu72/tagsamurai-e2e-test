---
id: TC-AC-SG-E2E-080-popup-users-clear-field-filter-tanpa-hasil-dan-sort-name-email-position
title: "Popup Users: Clear Field, Search Tanpa Hasil, dan Sort Name, Email, Position"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-294
  - TC-AC-SG-295
  - TC-AC-SG-296
  - TC-AC-SG-297
  - TC-AC-SG-298
coverage:
  web: automated
---

# Popup Users: Clear Field, Search Tanpa Hasil, dan Sort Name, Email, Position

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default spec.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak ditulis spec ini): entitas Principal `Pohon Uji Utama` (Pre-setup #16, 14 group), Total User per node (#17), penugasan Group Role dan Group Manager (#18), Total Member (#19), Last Updated dan Modified By (#20). Node `Region A`: Total User 5 (`Budi Santoso` Total Control, `Rina Wijaya` Read Only, `Andi Pratama` Group Manager dengan Position `Manager` dan Division `Operations`, `Sari Dewi` Group Role `Manage partner` dan `Manage allocation` tampil `2 roles`, `Dewi Lestari` Group Role `Manage active client`); Total Member 4 bertipe Distributor (`Distributor Alpha` Active 14 Jul 2026, `Distributor Beta` Suspended 12 Jul 2026, `Distributor Delta` Active 11 Jul 2026, `Distributor Gamma` Suspended 10 Jul 2026). Tabel Data Uji Dinamis TC tidak memuat data untuk spec ini. Pre-setup #19 dan #20 dipakai sebagai precondition TC, tidak diasersi.
- Data tambahan (disediakan tim FE): sedikitnya dua nilai Position distinct di antara user `Region A`. Pre-setup #18 hanya menyebut Position `Manager` untuk `Andi Pratama` (lihat Temuan untuk QA).
- Kemampuan teknis: Fixture BE (pembacaan state BE, seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`). Nilai data uji dirujuk lewat `Fixture.settingsGroup.<kunci>` (berkas `fixtures/settingsGroup.json` belum ada).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global dan tidak menulis data.

## Test Steps

1. Ketik Search `Region A` pada toolbar tabel utama, tekan Enter
2. Klik angka Total User pada baris `Region A`

### TC-AC-SG-294: Clear Field dan penutupan panel tanpa Apply pada filter popup Users

3. Klik ikon Filter pada toolbar popup
4. Pilih Position `Manager` lalu klik `[Apply]`
5. Ubah pilihan Division menjadi `Operations` tanpa klik `[Apply]`, tutup panel, lalu buka panel Filter lagi
6. Verifikasi panel menampilkan kembali nilai ter-Apply terakhir: Position `Manager` terpilih
7. Verifikasi panel menampilkan kembali nilai ter-Apply terakhir: Division kosong
8. Klik `[Clear Field]`
9. Verifikasi seluruh kriteria filter dikosongkan
10. Klik `[Apply]` untuk memulihkan tabel tanpa filter

### TC-AC-SG-295: Filter popup Users yang tidak cocok menampilkan empty state filtered

11. Ketik Search `zzzxxx` pada toolbar popup, tekan Enter
12. Verifikasi empty state `No results found` dengan Description `Try adjusting your search or filter.`
13. Verifikasi popup Users tetap terbuka
14. Klik `(←)` pada kotak Search popup untuk menutup input dan mereset tabel

### TC-AC-SG-296: Sort popup Users kolom Name: siklus tiga klik

15. Klik header Name sekali
16. Verifikasi klik pertama mengurutkan Name ascending (A-Z)
17. Klik header Name kedua kali
18. Verifikasi klik kedua mengurutkan Name descending
19. Klik header Name ketiga kali
20. Verifikasi klik ketiga netral kembali ke Name A-Z

### TC-AC-SG-297: Sort popup Users kolom Email: siklus tiga klik

21. Klik header Email sekali
22. Verifikasi klik pertama mengurutkan Email ascending (A-Z)
23. Klik header Email kedua kali
24. Verifikasi klik kedua mengurutkan Email descending
25. Klik header Email ketiga kali
26. Verifikasi klik ketiga netral kembali ke Name A-Z

### TC-AC-SG-298: Sort popup Users kolom Position: siklus tiga klik

27. Klik header Position sekali
28. Verifikasi klik pertama mengurutkan Position ascending (A-Z)
29. Klik header Position kedua kali
30. Verifikasi klik kedua mengurutkan Position descending
31. Klik header Position ketiga kali
32. Verifikasi klik ketiga netral kembali ke Name A-Z
33. Tutup popup lewat `[✕]`
34. Klik `(←)` pada kotak Search tabel utama untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target `Region A`, R-16), langkah `[Apply]` sesudah `[Clear Field]` (memulihkan tabel, S-09), klik `(←)` pada Search popup, penutupan popup, dan klik `(←)` pada Search tabel utama di akhir. Tiap TC sort berakhir pada sort netral (S-09). Popup dibuka satu kali untuk seluruh TC.
- Temuan untuk QA:
  - TC-AC-SG-295 berjudul "Filter ... tidak cocok" tetapi langkah dan Expected memakai Search `zzzxxx`; spec mengikuti langkah TC (Search).
  - TC-AC-SG-294 tidak menyebut nilai Position dan Division; spec memakai Position `Manager` dan Division `Operations` (Pre-setup #18, `Andi Pratama`). Hasil `[Clear Field]` diasersi pada kriteria panel; TC tidak menyatakan tabel kembali tanpa filter sebelum `[Apply]`.
  - Position user lain di `Region A` tidak tertulis di Pre-setup #18 (hanya `Andi Pratama` = `Manager`); kebutuhan data tambahan untuk sort Position ada di Prerequisites.
  - Perilaku panel Filter sesudah `[Apply]` di popup tidak dinyatakan PRD (T12); spec mengasumsikan panel tetap terbuka (pola spec 078 dan 079), sehingga klik ikon Filter berikutnya tidak diulang. Perlu konfirmasi FE.
