---
id: TC-GS-ROLE-E2E-029-assign-total-control-validasi-ineligible-user-v11-dan-campuran
title: "Validasi User Tidak Eligible (V-11) dan Penanganan Campuran V-10 + V-11 pada Assign Total Control"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-292
  - TC-GS-ROLE-301
  - TC-GS-ROLE-302
  - TC-GS-ROLE-305
coverage:
  web: automated
---

# Validasi User Tidak Eligible (V-11) dan Penanganan Campuran V-10 + V-11 pada Assign Total Control

## Prerequisites

- Dual session context
- Data Uji: Nina Kartika, Wawan Setiawan, Citra Dewanti
- Setup Hook: dualContext: sessionA, sessionB
- Login sbg Role: Total Control (Ahmad Fauzi)
- Eko Prasetyo (Total Control) login di sesi B

## Test Steps

### Assign Total Control saat Access Global Settings user terpilih dicabut sebelum submit (TC-GS-ROLE-292)

1. Sesi A: [+ Assign] > centang Nina Kartika dan Wawan Setiawan
2. Sesi B: modul User > Wawan Setiawan > hapus centang Access Global Settings > Save
3. Sesi A: klik [Assign]
4. Verifikasi Alert inline (danger): "Wawan Setiawan is no longer eligible. Please select another."
5. Verifikasi Seluruh submit ditolak: Nina Kartika tidak menjadi Total Control
6. Verifikasi Hanya centangan Wawan Setiawan yang hilang; Nina Kartika tetap tercentang
7. Verifikasi Daftar picker di-refetch tanpa Wawan Setiawan

### Assign Total Control saat dua user terpilih menjadi tidak eligible sebelum submit (alert jamak) (TC-GS-ROLE-301)

8. Sesi A: [+ Assign] > centang Ahmad Fauzan (ahmad.fz@client.com), Nina Kartika, dan Wawan Setiawan
9. Sesi B: assign Total Control ke Nina Kartika dan Wawan Setiawan
10. Sesi A: klik [Assign]
11. Verifikasi Alert inline (danger) jamak satu kalimat, pola "[User Name] and [User Name] are no longer eligible. Please select another.": kedua nama Nina Kartika dan Wawan Setiawan disebut (urutan nama tidak diasersi)
12. Verifikasi Seluruh submit ditolak: Ahmad Fauzan tidak menjadi Total Control
13. Verifikasi Centangan Nina Kartika dan Wawan Setiawan hilang; Ahmad Fauzan tetap tercentang; daftar picker di-refetch

### Assign Total Control dengan campuran user dihapus dan user tidak eligible dalam satu submit (TC-GS-ROLE-302)

14. Sesi A: [+ Assign] > centang Ahmad Fauzan (ahmad.fz@client.com), Nina Kartika, dan Wawan Setiawan
15. Sesi B: hapus user Nina Kartika di modul User dan assign Total Control ke Wawan Setiawan
16. Sesi A: klik [Assign]
17. Verifikasi Alert inline (danger) V-10 yang ditampilkan: "Nina Kartika no longer exists. Please select another."; alert V-11 untuk Wawan Setiawan tidak ditampilkan
18. Verifikasi Seluruh submit ditolak: Ahmad Fauzan tidak menjadi Total Control
19. Verifikasi Centangan Nina Kartika dan Wawan Setiawan hilang; Ahmad Fauzan tetap tercentang
20. Verifikasi Daftar picker di-refetch tanpa Nina Kartika

### Assign Total Control saat tiga user terpilih menjadi tidak eligible sebelum submit (alert jamak ≥3) (TC-GS-ROLE-305)

21. Sesi A: [+ Assign] > centang Ahmad Fauzan (ahmad.fz@client.com), Ahmad Fauzan (ahmad.fauzan@client.com), Nina Kartika, dan Wawan Setiawan
22. Sesi B: assign Total Control ke Ahmad Fauzan (ahmad.fauzan@client.com), Nina Kartika, dan Wawan Setiawan
23. Sesi A: klik [Assign]
24. Verifikasi Alert inline (danger) satu kalimat dengan pola "[User Name], [User Name], and [User Name] are no longer eligible. Please select another.": ketiga nama Ahmad Fauzan (ahmad.fauzan@client.com), Nina Kartika, dan Wawan Setiawan disebut dengan koma dan "and" sebelum nama terakhir (urutan nama tidak diasersi)
25. Verifikasi Seluruh submit ditolak: Ahmad Fauzan (ahmad.fz@client.com) tidak menjadi Total Control
26. Verifikasi Centangan ketiga user hilang; Ahmad Fauzan (ahmad.fz@client.com) tetap tercentang; daftar picker di-refetch

## Notes

- Memvalidasi alur skenario "Validasi User Tidak Eligible (V-11) dan Penanganan Campuran V-10 + V-11 pada Assign Total Control".
- Aturan PRD terkait: global-settings/role/PRD/role.md §6 V-11; global-settings/role/PRD/role.md ROLE-LOGIC-06a; global-settings/role/PRD/role.md ROLE-LOGIC-06c; global-settings/role/PRD/role.md §9.4.2; foundation/process/prd-process/error-handling-convention.md §5.5; global-settings/role/PRD/role.md §6 V-10.
- Sumber pemetaan test case granular: TC-GS-ROLE-292, TC-GS-ROLE-301, TC-GS-ROLE-302, TC-GS-ROLE-305.
