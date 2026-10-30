---
id: TC-GS-DIV-E2E-018-create-population-26-division-stay-on-form
title: "Create Population: 26 Division Berurutan dengan Stay on Form"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-30
coverage:
  web: automated
---

# Create Population: 26 Division Berurutan dengan Stay on Form

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: 6 Division (Finance FIN, Human Resources HR, Legal LGL, Operations OPS, Compliance CMP, Treasury TRS). Tabel harus berisi tepat 6 Division ini sebelum spec dimulai (precondition TC-GS-DIV-30: belum ada Division Data Uji Dinamis); suite berjalan serial (`parallel: false`) dan spec lain membersihkan Division miliknya sendiri, sehingga tidak ada Division lain selama spec ini berjalan. Spec tidak mengubah Division Pre-setup.
- Layar awal `Global Settings > User > Division` dibuka di hook `beforeEach` (konvensi bagian 4).
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data dinamis D-02 (Population, 26 Division, Name dan Code literal): Accounting (ACC); Administration (ADM); Audit (AUD); Business Development (BD); Corporate Communication (CCM); Customer Service (CSV); Data Analytics (DA); Engineering (ENG); Facilities (FAC); General Affairs (GA); Information Technology (IT); Internal Control (IC); Logistics (LOG); Marketing (MKT); Procurement (PRC); Product Management (PM); Production (PRD); Quality Assurance (QA); Research and Development (RND); Risk Management (RSK); Sales (SLS); Security (SEC); Strategy (STR); Supply Chain (SC); Training (TRN); Warehouse (WH). Dibuat lewat UI oleh spec ini; satu-satunya spec yang membuat Population lewat UI. Nama literal tanpa suffix `{runId}` karena asersi jumlah 32 baris dan 4 halaman bergantung pada kumpulan nama ini (pengecualian Population D-02, S-12: seeding idempotent, sisa dihapus di hook `before`, cleanup milik spec, suite serial).
- Hook `before`: hapus lewat API sisa Population D-02 dari run atau spec sebelumnya (26 Division di atas) bila ada, sehingga tabel awal tepat 6 Division Pre-setup.
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): hapus lewat API seluruh 26 Division D-02 yang dibuat spec ini bila masih ada.
- Kemampuan teknis: pembacaan fokus keyboard pada field Division Name; pembacaan state checkbox; pembacaan pagination (jumlah baris per halaman dan jumlah halaman).
- State global: tidak ada yang diubah.

## Test Steps

### TC-GS-DIV-30: Population: Create 26 Division berurutan dengan Stay on this form dicentang

1. Klik `[+ Division]`
2. Centang checkbox `Stay on this form after submitting`
3. Isi Division Name `Accounting` dan Code `ACC`, klik `[Submit]`
4. Verifikasi toast sukses: `Success, division has been created.`
5. Verifikasi modal tetap terbuka
6. Verifikasi Division Name kosong
7. Verifikasi Code kosong
8. Verifikasi fokus kembali ke Division Name
9. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
10. Isi Division Name `Administration` dan Code `ADM`, klik `[Submit]`
11. Verifikasi toast sukses: `Success, division has been created.`
12. Isi Division Name `Audit` dan Code `AUD`, klik `[Submit]`
13. Verifikasi toast sukses: `Success, division has been created.`
14. Isi Division Name `Business Development` dan Code `BD`, klik `[Submit]`
15. Verifikasi toast sukses: `Success, division has been created.`
16. Isi Division Name `Corporate Communication` dan Code `CCM`, klik `[Submit]`
17. Verifikasi toast sukses: `Success, division has been created.`
18. Isi Division Name `Customer Service` dan Code `CSV`, klik `[Submit]`
19. Verifikasi toast sukses: `Success, division has been created.`
20. Isi Division Name `Data Analytics` dan Code `DA`, klik `[Submit]`
21. Verifikasi toast sukses: `Success, division has been created.`
22. Isi Division Name `Engineering` dan Code `ENG`, klik `[Submit]`
23. Verifikasi toast sukses: `Success, division has been created.`
24. Isi Division Name `Facilities` dan Code `FAC`, klik `[Submit]`
25. Verifikasi toast sukses: `Success, division has been created.`
26. Isi Division Name `General Affairs` dan Code `GA`, klik `[Submit]`
27. Verifikasi toast sukses: `Success, division has been created.`
28. Isi Division Name `Information Technology` dan Code `IT`, klik `[Submit]`
29. Verifikasi toast sukses: `Success, division has been created.`
30. Isi Division Name `Internal Control` dan Code `IC`, klik `[Submit]`
31. Verifikasi toast sukses: `Success, division has been created.`
32. Isi Division Name `Logistics` dan Code `LOG`, klik `[Submit]`
33. Verifikasi toast sukses: `Success, division has been created.`
34. Isi Division Name `Marketing` dan Code `MKT`, klik `[Submit]`
35. Verifikasi toast sukses: `Success, division has been created.`
36. Isi Division Name `Procurement` dan Code `PRC`, klik `[Submit]`
37. Verifikasi toast sukses: `Success, division has been created.`
38. Isi Division Name `Product Management` dan Code `PM`, klik `[Submit]`
39. Verifikasi toast sukses: `Success, division has been created.`
40. Isi Division Name `Production` dan Code `PRD`, klik `[Submit]`
41. Verifikasi toast sukses: `Success, division has been created.`
42. Isi Division Name `Quality Assurance` dan Code `QA`, klik `[Submit]`
43. Verifikasi toast sukses: `Success, division has been created.`
44. Isi Division Name `Research and Development` dan Code `RND`, klik `[Submit]`
45. Verifikasi toast sukses: `Success, division has been created.`
46. Isi Division Name `Risk Management` dan Code `RSK`, klik `[Submit]`
47. Verifikasi toast sukses: `Success, division has been created.`
48. Isi Division Name `Sales` dan Code `SLS`, klik `[Submit]`
49. Verifikasi toast sukses: `Success, division has been created.`
50. Isi Division Name `Security` dan Code `SEC`, klik `[Submit]`
51. Verifikasi toast sukses: `Success, division has been created.`
52. Isi Division Name `Strategy` dan Code `STR`, klik `[Submit]`
53. Verifikasi toast sukses: `Success, division has been created.`
54. Isi Division Name `Supply Chain` dan Code `SC`, klik `[Submit]`
55. Verifikasi toast sukses: `Success, division has been created.`
56. Isi Division Name `Training` dan Code `TRN`, klik `[Submit]`
57. Verifikasi toast sukses: `Success, division has been created.`
58. Isi Division Name `Warehouse` dan Code `WH`, klik `[Submit]`
59. Verifikasi toast sukses: `Success, division has been created.`
60. Verifikasi modal tetap terbuka
61. Verifikasi Division Name kosong
62. Verifikasi Code kosong
63. Verifikasi fokus kembali ke Division Name
64. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
65. Klik icon `[✕]` untuk menutup modal
66. Verifikasi modal tertutup
67. Verifikasi tidak ada dialog `Unsaved Changes`
68. Verifikasi tabel menampilkan 32 Division: 6 Pre-setup ditambah 26 Population
69. Verifikasi halaman 1 berisi 10 baris
70. Verifikasi tabel terbagi dalam 4 halaman

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Spec ini sengaja satu TC (TC-GS-DIV-30) karena menjadi sumber Population D-02; spec lain yang butuh Population men-seed-nya sendiri lewat API di hook `before` secara idempotent (dilewati bila sudah ada) dan tidak bergantung pada spec ini.
- Langkah 1, 2, 3 sampai 59, dan 65 mengikuti langkah 1, 2, 3, dan 4 TC sumber; tiap pengulangan "Isi Division Name dan Code, klik `[Submit]`" (langkah 3 sampai 59) untuk 26 pasangan ditutup asersi toast sukses (Expected a, berlaku untuk tiap Submit).
- Expected b (modal tetap terbuka, Division Name dan Code kosong, fokus kembali ke Division Name, checkbox tetap tercentang) diasersi pada Submit pertama (langkah 5 sampai 9) dan Submit terakhir (langkah 60 sampai 64); perilaku form identik antar pengulangan, dan form yang tidak ter-reset pada pengulangan di antaranya membuat pengisian berikutnya gagal.
- Expected c diasersi sesudah modal ditutup (langkah 68 sampai 70) dan Expected d pada langkah 67 (tidak ada dialog `Unsaved Changes` sesudah menutup lewat `[✕]` pada form kosong).
- Spec melewati sekitar 35 langkah (70 langkah) karena 26 pengulangan Create untuk satu topik aksi dan satu kelas harness (aksi sukses, volume) dengan satu akun dan satu form Stay on this form yang dipakai terus; tiap pengulangan memakai pasangan Name dan Code sendiri, dan memecahnya hanya menambah login, hook, dan pembukaan form serta menghilangkan state form yang diuji.
- Asersi 32 baris, halaman 1 berisi 10 baris, dan 4 halaman (langkah 68 sampai 70) bergantung pada tabel awal tepat 6 Division dan nama Population literal.
