---
id: TC-AC-CS-E2E-087-list-filter-screening-dan-opsi-dropdown
title: "List Filter: Screening dan Opsi Dropdown"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-325
  - TC-AC-CS-326
  - TC-AC-CS-327
  - TC-AC-CS-328
  - TC-AC-CS-329
coverage:
  web: automated
---

# List Filter: Screening dan Opsi Dropdown

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Hendra Wijaya, Total Control Principal PT ABC (Pre-setup #1), password `Spectra.env.AC_SUB_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (fixture disediakan tim FE); password hanya lewat env, tidak ditulis di spec atau fixture.
- Data Pre-setup (kelas e, baca-saja): dataset uji #82, yaitu 120 baris term di tab Current dan 60 baris di tab History untuk Client campuran (Plan Owner PT Maju Bersama dan CV Karya Mandiri); jumlah total baris diturunkan dari seeding dataset, bukan dibaca dari satu halaman tabel (bagian 8b butir 10). Spec tidak menulis ke dataset; Search, Filter, Sort, dan Pagination dibersihkan sebagai langkah penghubung antar blok TC.
- Kemampuan teknis (disediakan tim FE/BE): tidak ada kebutuhan di luar dataset #82.
- Hook `beforeEach` suite membuka Allocation > Client Subscription pada tab Current dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat suite.md).
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-325: Screening Filter Panel List

1. Klik ikon Filter di toolbar
2. Verifikasi ikon Filter berubah gelap saat panel terbuka
3. Verifikasi Filter Panel tampil di bawah toolbar
4. Verifikasi field Body: Client (multi-select searchable, placeholder "All clients"), Product ("All products"), Plan ("All plans"), Status ("All statuses"), Start Date (date range picker, "Select date"), End Date ("Select date"), Grace End ("Select date"), Plan Owner ("All entities"), Type ("All types")
5. Verifikasi maksimal empat field per baris
6. Verifikasi Footer memuat `[Clear Field]` di kiri dan `[Apply]` di kanan

### TC-AC-CS-326: Apply dan Clear Field pada Filter Panel

7. Pilih Product `FAMS`, klik `[Apply]`
8. Verifikasi tabel menampilkan sedikitnya satu baris
9. Verifikasi hanya baris Product `FAMS` tampil
10. Klik `[Clear Field]`
11. Verifikasi `[Clear Field]` mengosongkan seluruh field panel
12. Verifikasi panel tetap terbuka
13. Klik `[Apply]`
14. Verifikasi tabel kembali menampilkan semua baris tab "Current"

### TC-AC-CS-327: Indikator titik pada ikon Filter selama ada filter ter-Apply

15. Pilih Product `FAMS`, klik `[Apply]`, lalu tutup panel dengan klik ikon Filter
16. Verifikasi ikon Filter menampilkan badge titik tanpa angka walau panel tertutup
17. Klik ikon Filter untuk membuka panel, klik `[Clear Field]`, lalu klik `[Apply]`
18. Verifikasi titik pada ikon Filter hilang

### TC-AC-CS-328: Menutup panel tanpa Apply membuang perubahan yang belum di-Apply

19. Pilih Product `FAMS`, klik `[Apply]`
20. Ubah Product menjadi `SAMS` tanpa Apply, lalu klik ikon Filter untuk menutup panel
21. Verifikasi tabel menampilkan sedikitnya satu baris
22. Verifikasi tabel tetap menampilkan hasil filter ter-Apply terakhir (`FAMS`)
23. Klik ikon Filter untuk membuka kembali panel
24. Verifikasi panel menampilkan nilai ter-Apply terakhir `FAMS`, bukan draft `SAMS`
25. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-CS-329: Opsi dropdown Client, Plan, dan Plan Owner di-populate dari baris tabel

26. Buka dropdown Client
27. Verifikasi sedikitnya satu opsi Client lain tampil di dropdown Client
28. Verifikasi opsi Client hanya Client yang punya baris pada tab "Current" yang sedang match
29. Verifikasi `Client Tanpa Subscription` tidak ada karena tidak muncul di tabel
30. Tutup dropdown Client, lalu buka dropdown Plan
31. Verifikasi sedikitnya satu opsi Plan lain tampil di dropdown Plan
32. Verifikasi opsi Plan hanya nilai yang ada pada baris tab aktif
33. Tutup dropdown Plan, lalu buka dropdown Plan Owner
34. Verifikasi sedikitnya satu opsi Plan Owner lain tampil di dropdown Plan Owner
35. Verifikasi opsi Plan Owner hanya nilai yang ada pada baris tab aktif dan berformat `[Nama] (Type)`
36. Tutup dropdown Plan Owner dan panel Filter

## Notes

- Alasan spec lebih dari sekitar 35 langkah: seluruh blok memakai satu Filter Panel, satu layar, dan satu dataset baca-saja (#82); tiap blok berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung: penutupan dropdown dan panel, serta `[Clear Field]` dan `[Apply]` untuk memulihkan filter di akhir blok TC-AC-CS-328.
- Panel Filter tidak menutup setelah `[Apply]` (TC-AC-CS-326 langkah 3 dan TC-AC-CS-327 langkah 2 meminta menutup panel dengan klik ikon Filter); urutan langkah mengikuti keadaan panel.
- Temuan untuk QA: (1) TC-AC-CS-325 Expected b i memuat sembilan field dalam satu butir; spec menuliskannya satu Verifikasi daftar elemen (S-01). (2) TC-AC-CS-329 tidak menyebut tab yang aktif selain "Current" dari precondition; opsi Client dan Plan Owner dibandingkan dengan baris tab "Current" di dataset #82. (3) TC-AC-CS-326 tidak menyebut apakah Footer menutup panel setelah `[Apply]`; spec mengikuti urutan TC-AC-CS-327.
