---
id: TC-AC-ACC-E2E-243-sort-station-list-teks-numerik-last-active-dan-nilai-kosong
title: "Sort Station List: Kolom Teks, Numerik, Last Active, dan Nilai Kosong Reader Group"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-313
  - TC-AC-ACC-793
  - TC-AC-ACC-794
  - TC-AC-ACC-795
  - TC-AC-ACC-844
coverage:
  web: automated
---

# Sort Station List: Kolom Teks, Numerik, Last Active, dan Nilai Kosong Reader Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup (hanya dibaca, tidak diubah): Client C-01 "PT Sejahtera Abadi" dengan Station List: "Gerbang Gudang A" (Active, Reader Group (Fixed Asset) "Gudang Pusat", Reader Group (Supply) kosong, RDR-0001, Ports 4, Tablets 2, Last Active 08 Jul 2026 09:30); "Gerbang Gudang B" (Inactive, "Gudang Pusat", "Supply Utama", RDR-0002, Ports 4, Tablets 1, Last Active 08 Jul 2026 08:10); "Gerbang Lama" (Deactivated, kedua group kosong, RDR-0003, Ports 2, Tablets 0, Last Active 01 Mar 2026). Setiap kolom yang diurutkan punya sedikitnya dua nilai distinct. Urutan default: Reader Name A-Z.
- Parameter blok TC-AC-ACC-793 (langkah 15 sampai 21):

| Kolom | Urutan ascending | Urutan descending |
|---|---|---|
| Reader Name | Gerbang Gudang A, Gerbang Gudang B, Gerbang Lama | Gerbang Lama, Gerbang Gudang B, Gerbang Gudang A |
| Reader ID | Gerbang Gudang A (RDR-0001), Gerbang Gudang B (RDR-0002), Gerbang Lama (RDR-0003) | Gerbang Lama, Gerbang Gudang B, Gerbang Gudang A |
| Status | Gerbang Gudang A (Active), Gerbang Lama (Deactivated), Gerbang Gudang B (Inactive) | Gerbang Gudang B, Gerbang Lama, Gerbang Gudang A |

- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Detail diatur hook suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

1. Ketik Search "PT Sejahtera Abadi" di List Client, tekan Enter, klik Company Name "PT Sejahtera Abadi", lalu klik Tab Asset Control

### TC-AC-ACC-313: Sort Reader Group (Fixed Asset): nilai kosong

2. Klik header Reader Group (Fixed Asset) satu kali
3. Verifikasi Gerbang Lama (`—`) pada posisi 3
4. Klik header Reader Group (Fixed Asset) untuk kedua kali
5. Verifikasi Gerbang Lama (`—`) pada posisi 1
6. Klik header Reader Group (Fixed Asset) untuk ketiga kali
7. Verifikasi urutan kembali ke default Reader Name A-Z: Gerbang Gudang A, Gerbang Gudang B, Gerbang Lama

### TC-AC-ACC-844: Sort Reader Group (Supply): nilai kosong di akhir saat ascending

8. Klik header Reader Group (Supply)
9. Verifikasi Gerbang Gudang B (Supply Utama) pada posisi 1, lalu Gerbang Gudang A dan Gerbang Lama (`—`) pada posisi 2 dan 3
10. Klik header Reader Group (Supply) lagi
11. Verifikasi Gerbang Gudang A dan Gerbang Lama (`—`) pada posisi 1 dan 2, lalu Gerbang Gudang B pada posisi 3
12. Klik header Reader Group (Supply) ketiga kali
13. Verifikasi urutan kembali ke default Reader Name A-Z: Gerbang Gudang A, Gerbang Gudang B, Gerbang Lama

### TC-AC-ACC-793: Sort kolom teks Reader Name, Reader ID, dan Status

14. Verifikasi urutan awal (default Reader Name A-Z): Gerbang Gudang A, Gerbang Gudang B, Gerbang Lama
15. Untuk setiap baris tabel "Parameter blok TC-AC-ACC-793" (langkah 15 sampai 21): klik header kolom satu kali
16. Verifikasi urutan ascending sesuai tabel
17. Klik header kolom untuk kedua kali
18. Verifikasi urutan descending sesuai tabel
19. Klik header kolom untuk ketiga kali
20. Verifikasi indikator sort kolom nonaktif
21. Verifikasi urutan kembali ke default Reader Name A-Z

### TC-AC-ACC-794: Sort kolom numerik Ports dan Tablets

22. Klik header kolom Ports satu kali
23. Verifikasi Gerbang Lama (2) pada posisi 1 lalu Gerbang Gudang A dan Gerbang Gudang B (4) pada posisi 2 dan 3 (urutan antar keduanya tidak dinilai)
24. Klik header kolom Ports untuk kedua kali
25. Verifikasi Gerbang Gudang A dan Gerbang Gudang B (4) pada posisi 1 dan 2 (urutan antar keduanya tidak dinilai) lalu Gerbang Lama (2) pada posisi 3
26. Klik header kolom Ports untuk ketiga kali
27. Verifikasi indikator sort Ports nonaktif
28. Verifikasi urutan kembali ke default Reader Name A-Z
29. Klik header kolom Tablets satu kali
30. Verifikasi urutan ascending: Gerbang Lama (0), Gerbang Gudang B (1), Gerbang Gudang A (2)
31. Klik header kolom Tablets untuk kedua kali
32. Verifikasi urutan descending: Gerbang Gudang A (2), Gerbang Gudang B (1), Gerbang Lama (0)
33. Klik header kolom Tablets untuk ketiga kali
34. Verifikasi indikator sort Tablets nonaktif
35. Verifikasi urutan kembali ke default Reader Name A-Z

### TC-AC-ACC-795: Sort kolom Last Active

36. Klik header kolom Last Active satu kali
37. Verifikasi ascending (Oldest First): Gerbang Lama (01 Mar 2026), Gerbang Gudang B (08 Jul 2026 08:10), Gerbang Gudang A (08 Jul 2026 09:30)
38. Klik header kolom Last Active untuk kedua kali
39. Verifikasi descending (Newest First): Gerbang Gudang A, Gerbang Gudang B, Gerbang Lama
40. Klik header kolom Last Active untuk ketiga kali
41. Verifikasi indikator sort Last Active nonaktif
42. Verifikasi urutan kembali ke default Reader Name A-Z

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 (Search dan buka Detail Client; hook suite hanya membuka List Client).
- Langkah 15 sampai 21 diulang untuk 3 baris tabel parameter (21 langkah setelah ekspansi). Urutan posisi kolom Status ascending mengikuti Expected TC-AC-ACC-793 butir d (Active, Deactivated, Inactive).
- Spec ini melewati sekitar 35 langkah setelah ekspansi. Alasan: semua blok satu topik (Sort Station List) pada satu dataset Pre-setup baca-saja; tiap blok diakhiri klik ketiga yang mengembalikan urutan default sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-ACC-313 Expected b menyebut klik kedua "descending" dengan Gerbang Lama pada posisi 1; Expected tidak menyebut urutan Gerbang Gudang A dan Gerbang Gudang B (nilai Fixed Asset sama) sehingga tidak diasersi.
