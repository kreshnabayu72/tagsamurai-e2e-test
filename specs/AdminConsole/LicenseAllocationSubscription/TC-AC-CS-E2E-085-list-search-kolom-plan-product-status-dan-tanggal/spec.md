---
id: TC-AC-CS-E2E-085-list-search-kolom-plan-product-status-dan-tanggal
title: "List Search: Kolom Plan, Product, Status, dan Tanggal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-315
  - TC-AC-CS-316
  - TC-AC-CS-317
  - TC-AC-CS-318
  - TC-AC-CS-324
coverage:
  web: automated
---

# List Search: Kolom Plan, Product, Status, dan Tanggal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Hendra Wijaya, Total Control Principal PT ABC (Pre-setup #1), password `Spectra.env.AC_SUB_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (fixture disediakan tim FE); password hanya lewat env, tidak ditulis di spec atau fixture.
- Data Pre-setup (kelas e, baca-saja): dataset uji #82, yaitu 120 baris term di tab Current dan 60 baris di tab History untuk Client campuran (Plan Owner PT Maju Bersama dan CV Karya Mandiri); jumlah total baris diturunkan dari seeding dataset, bukan dibaca dari satu halaman tabel (bagian 8b butir 10). Spec tidak menulis ke dataset; Search, Filter, Sort, dan Pagination dibersihkan sebagai langkah penghubung antar blok TC.
- Hook `beforeEach` suite membuka Allocation > Client Subscription pada tab Current dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat suite.md).
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-315: Search kolom Plan: nama plan dan label badge Trial atau Custom

1. Ketik Search `professional`, tekan Enter
2. Verifikasi baris Plan `Professional` tampil
3. Ganti isi kotak search dengan `Custom`, tekan Enter
4. Verifikasi baris Custom Plan `Mitra Premium` tampil karena label badge ikut dicocokkan
5. Ganti isi kotak search dengan `Trial`, tekan Enter
6. Verifikasi baris Trial tampil karena label badge ikut dicocokkan

### TC-AC-CS-316: Search kolom Product: nilai enum FAMS, SAMS, SIEM

7. Ganti isi kotak search dengan `siem`, tekan Enter
8. Verifikasi baris Product `SIEM` tampil untuk keyword huruf kecil
9. Ganti isi kotak search dengan `FAMS`, tekan Enter
10. Verifikasi baris Product `FAMS` tampil
11. Verifikasi tidak ada baris Product `SAMS` maupun `SIEM` tampil

### TC-AC-CS-317: Search kolom Status: label badge

12. Ganti isi kotak search dengan `waiting`, tekan Enter
13. Verifikasi baris berstatus Waiting for Approval tampil
14. Ganti isi kotak search dengan `GRACE`, tekan Enter
15. Verifikasi baris berstatus Grace tampil tanpa membedakan huruf besar kecil, sehingga kolom Status masuk cakupan Search

### TC-AC-CS-318: Search tidak mencocokkan kolom tanggal

16. Ganti isi kotak search dengan `31/12/26`, tekan Enter
17. Verifikasi empty state "No results found" dengan Description "Try adjusting your search or filter." tampil
18. Verifikasi keyword `31/12/26` tidak mencocokkan baris mana pun
19. Ganti isi kotak search dengan `Jan`, tekan Enter
20. Verifikasi empty state "No results found" dengan Description "Try adjusting your search or filter." tampil
21. Verifikasi keyword `Jan` tidak mencocokkan baris karena nilai Start Date atau End Date

### TC-AC-CS-324: Type adalah field filter dan bukan kolom pencarian

22. Ganti isi kotak search dengan `Paid`, tekan Enter
23. Verifikasi empty state "No results found" tampil bila tidak ada plan, client, atau owner yang memuat teks `Paid`
24. Verifikasi keyword `Paid` tidak menampilkan baris hanya karena Type term adalah Paid

## Notes

- Langkah penghubung: tidak ada selain penggantian isi kotak Search antar kata kunci (bagian 8b butir 9).
- Anchor positif: Verifikasi empty state "No results found" mendahului tiap asersi absence pada TC-AC-CS-318 dan TC-AC-CS-324 (8b.2); untuk keyword `Jan` empty state diasersi sebagai Verifikasi sendiri sebelum absence.
- Temuan untuk QA: (1) TC-AC-CS-317 butir c ("Kolom Status masuk cakupan Search sekaligus Filter") adalah kesimpulan dari butir a dan b dan tidak punya langkah observasi terpisah di Filter; spec menggabungkannya pada Verifikasi hasil `GRACE` (S-03). (2) TC-AC-CS-318 butir d ("Penyaringan tanggal hanya melalui Filter Panel") adalah kesimpulan dan tidak diasersi terpisah. (3) TC-AC-CS-324 butir c ("Penyaringan Type tersedia lewat Filter Panel") adalah kesimpulan dan tidak diasersi terpisah; butir b bersyarat ("bila tidak ada plan, client, atau owner yang memuat teks `Paid`") dan precondition tidak menyebut data itu, sehingga spec mengasersi empty state sesuai dataset #82.
