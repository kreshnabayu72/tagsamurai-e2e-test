---
id: TC-GS-BRAND-E2E-042-used-by-items-link-detail-dan-hover
title: "Link Angka Used By (Items): Hover, Fokus, dan Pembukaan Brand Detail"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-268
  - TC-GS-BRAND-269
  - TC-GS-BRAND-271
  - TC-GS-BRAND-280
coverage:
  web: automated
---

# Link Angka Used By (Items): Hover, Fokus, dan Pembukaan Brand Detail

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi); password dari `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before` (seedSession).
- Data Pre-setup (tetap di environment, spec ini tidak membuat atau mengubah data): 12 brand Client A. Yang dipakai: Vertex Labs (Used By `5`; Asset Name Laptop dengan 5 Model, Monitor, tiga Supply), Orion Tech (`0`, bebas relasi), Acme Corp (`1`, FAMS Asset Name Forklift), Kestrel (`2`, FAMS Laptop dan Supply Laptop).
- Baris yang dirujuk dicari lewat Search `<nama brand>` karena bisa berada di halaman selain halaman pertama (10 per halaman).
- State global: tidak ada yang diubah.
- Hook `beforeEach`: kembali ke layar Global Settings > Master Reference > Brand.
- Kemampuan teknis: hover dan navigasi keyboard (Tab) dengan pembacaan warna teks, text-decoration, dan focus ring.

## Test Steps

1. Buka layar Global Settings > Master Reference > Brand

### TC-GS-BRAND-280: Hover dan fokus link angka Used By (Items) sama dengan pola link Brand Name

2. Search `Vertex Labs`, tekan Enter
3. Perhatikan angka `5` pada baris Vertex Labs tanpa hover
4. Verifikasi angka `5` berupa teks link netral tanpa hover
5. Arahkan kursor (hover) ke angka `5` dan catat warna teks serta dekorasi teksnya
6. Verifikasi warna teks berubah mengikuti warna primary Global Settings (hitam) tanpa garis bawah
7. Pindahkan kursor keluar dari angka `5`
8. Verifikasi warna angka `5` kembali netral
9. Arahkan kursor (hover) ke teks Brand Name `Vertex Labs`
10. Verifikasi hover teks Brand Name memiliki warna dan dekorasi teks yang sama dengan hover angka `5` yang dicatat pada langkah 5 (pola TC-GS-BRAND-11)
11. Tekan Tab hingga fokus keyboard berada di angka `5`
12. Verifikasi fokus keyboard menampilkan focus ring pada angka `5`

### TC-GS-BRAND-268: Klik angka Used By (Items) membuka Modal Brand Detail

13. Klik angka `5` pada baris Vertex Labs
14. Verifikasi Modal Brand Detail Vertex Labs terbuka
15. Verifikasi General Info `Total Item: 5`
16. Verifikasi tidak ada popup `Item Types` atau `+N More`
17. Tutup Modal Brand Detail
18. Klik link nama Vertex Labs
19. Verifikasi Modal Brand Detail yang terbuka sama dengan hasil klik angka `5` (Vertex Labs, `Total Item: 5`)
20. Tutup Modal Brand Detail

### TC-GS-BRAND-269: Klik angka 0 pada kolom Used By (Items) membuka Brand Detail dengan empty state accordion

21. Search `Orion Tech`, tekan Enter
22. Klik angka `0` pada baris Orion Tech
23. Verifikasi Modal Brand Detail Orion Tech terbuka
24. Verifikasi General Info `Total Item: 0`
25. Verifikasi accordion Item Type List menampilkan empty state `No item types linked` / `No products or items currently reference this brand.`
26. Tutup Modal Brand Detail

### TC-GS-BRAND-271: Angka Used By (Items) sama dengan Total Item di Detail (instance Client)

27. Search `Vertex Labs`, tekan Enter
28. Catat angka Used By (Items) baris Vertex Labs
29. Klik link nama Vertex Labs untuk membuka Detail
30. Verifikasi angka tabel sama dengan `Total Item` Detail Vertex Labs: `5`
31. Verifikasi tidak ada Device SKU yang dihitung pada Detail Vertex Labs (instance Client)
32. Tutup Modal Brand Detail
33. Search `Acme Corp`, tekan Enter
34. Catat angka Used By (Items) baris Acme Corp
35. Klik link nama Acme Corp untuk membuka Detail
36. Verifikasi angka tabel sama dengan `Total Item` Detail Acme Corp: `1`
37. Verifikasi tidak ada Device SKU yang dihitung pada Detail Acme Corp (instance Client)
38. Tutup Modal Brand Detail
39. Search `Kestrel`, tekan Enter
40. Catat angka Used By (Items) baris Kestrel
41. Klik link nama Kestrel untuk membuka Detail
42. Verifikasi angka tabel sama dengan `Total Item` Detail Kestrel: `2`
43. Verifikasi tidak ada Device SKU yang dihitung pada Detail Kestrel (instance Client)

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Urutan TC dalam spec: 280 (hover/fokus, tanpa aksi) di awal sebagai screening, lalu 268, 269, 271. Spec tidak membuat atau menghapus data sehingga tidak butuh seeding atau cleanup.
- Spec sekitar 43 langkah karena TC-GS-BRAND-271 menguji tiga brand; seluruhnya satu kelas harness (UI biasa), satu akun, tanpa dependensi data antar-bagian, sehingga tidak dipecah.
- Langkah penghubung: langkah 2, 21, 27, 33, dan 39 (Search nama brand untuk menemukan baris, karena baris bisa berada di halaman selain halaman pertama) serta langkah 17, 20, 26, 32, dan 38 (menutup Modal Brand Detail sebelum langkah berikutnya).
- Langkah 9 dan 10 mewujudkan butir "sama dengan hover teks Brand Name (TC-GS-BRAND-11)" pada Expected Result TC-GS-BRAND-280 sebagai perbandingan langsung; langkah 18 dan 19 mewujudkan "sama seperti klik link nama" pada TC-GS-BRAND-268.
