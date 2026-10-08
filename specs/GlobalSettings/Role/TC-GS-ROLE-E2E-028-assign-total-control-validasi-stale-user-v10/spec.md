---
id: TC-GS-ROLE-E2E-028-assign-total-control-validasi-stale-user-v10
title: "Validasi Stale User (V-10) pada Assign Total Control: Penanganan Kandidat Dihapus atau Di-Assign Sesi Lain (Alert Tunggal & Jamak)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-63
  - TC-GS-ROLE-66
  - TC-GS-ROLE-300
  - TC-GS-ROLE-304
coverage:
  web: automated
---

# Validasi Stale User (V-10) pada Assign Total Control: Penanganan Kandidat Dihapus atau Di-Assign Sesi Lain (Alert Tunggal & Jamak)

## Prerequisites

- Dual session context (Sesi A dan Sesi B Total Control)
- Data Uji: Nina Kartika, Wawan Setiawan, Citra Dewanti
- Setup Hook: dualContext: sessionA, sessionB
- Login sbg Role: Total Control (Ahmad Fauzi)
- User berada di Global Settings > Role & Permission > Total Control
- Eko Prasetyo (Total Control) login di sesi B

## Test Steps

### Klik ganda [Assign] Popup Assign Total Control (TC-GS-ROLE-63)

1. Klik [+ Assign]
2. Centang Nina Kartika
3. Klik [Assign] dua kali cepat
4. Verifikasi Setelah klik pertama tombol [Assign] masuk state loading/disabled
5. Verifikasi Satu toast sukses: "Success, Total Control has been assigned."
6. Verifikasi Modal Changelog Tab Total Control memuat tepat 1 entry Assign untuk Nina Kartika

### Assign Total Control saat user terpilih menjadi tidak eligible sebelum submit (TC-GS-ROLE-66)

7. Sesi A: [+ Assign] > centang Nina Kartika dan Wawan Setiawan
8. Sesi B: assign Total Control ke Wawan Setiawan
9. Sesi A: klik [Assign]
10. Verifikasi Alert inline (danger), template "[User Name] is no longer eligible. Please select another.": "Wawan Setiawan is no longer eligible. Please select another."
11. Verifikasi Seluruh submit ditolak: Nina Kartika tidak menjadi Total Control
12. Verifikasi Hanya centangan Wawan Setiawan yang hilang; Nina Kartika tetap tercentang; daftar picker di-refetch
13. Verifikasi Changelog Tab Total Control tidak memuat entry Assign baru dari sesi A untuk kedua user

### Assign Total Control saat dua user terpilih dihapus admin lain sebelum submit (alert jamak) (TC-GS-ROLE-300)

14. Sesi A: [+ Assign] > centang Ahmad Fauzan (ahmad.fz@client.com), Nina Kartika, dan Wawan Setiawan
15. Sesi B: hapus user Nina Kartika dan Wawan Setiawan di modul User
16. Sesi A: klik [Assign]
17. Verifikasi Alert inline (danger) jamak satu kalimat, pola "[User Name] and [User Name] no longer exist. Please select another.": kedua nama Nina Kartika dan Wawan Setiawan disebut (urutan nama tidak diasersi)
18. Verifikasi Seluruh submit ditolak: Ahmad Fauzan tidak menjadi Total Control
19. Verifikasi Popup tetap terbuka; centangan Nina Kartika dan Wawan Setiawan hilang, Ahmad Fauzan tetap tercentang
20. Verifikasi Daftar picker di-refetch tanpa kedua user

### Assign Total Control saat tiga user terpilih dihapus admin lain sebelum submit (alert jamak ≥3) (TC-GS-ROLE-304)

21. Sesi A: [+ Assign] > centang Ahmad Fauzan (ahmad.fz@client.com), Ahmad Fauzan (ahmad.fauzan@client.com), Nina Kartika, dan Wawan Setiawan
22. Sesi B: hapus user Ahmad Fauzan (ahmad.fauzan@client.com), Nina Kartika, dan Wawan Setiawan di modul User
23. Sesi A: klik [Assign]
24. Verifikasi Alert inline (danger) satu kalimat dengan pola "[User Name], [User Name], and [User Name] no longer exist. Please select another.": ketiga nama Ahmad Fauzan (ahmad.fauzan@client.com), Nina Kartika, dan Wawan Setiawan disebut dengan koma dan "and" sebelum nama terakhir (urutan nama tidak diasersi)
25. Verifikasi Seluruh submit ditolak: Ahmad Fauzan (ahmad.fz@client.com) tidak menjadi Total Control
26. Verifikasi Centangan ketiga user hilang; Ahmad Fauzan (ahmad.fz@client.com) tetap tercentang; daftar picker di-refetch

## Notes

- Memvalidasi alur skenario "Validasi Stale User (V-10) pada Assign Total Control: Penanganan Kandidat Dihapus atau Di-Assign Sesi Lain (Alert Tunggal & Jamak)".
- Aturan PRD terkait: global-settings/role/PRD/role.md §9.4.2 Semua aksi tulis D6 klik ganda; foundation/process/prd-process/error-handling-convention.md §5.1; global-settings/role/PRD/role.md §6 V-11; global-settings/role/PRD/role.md ROLE-LOGIC-06c; global-settings/role/PRD/role.md §6 V-10; global-settings/role/PRD/role.md §9.4.2; foundation/process/prd-process/error-handling-convention.md §5.5.
- Sumber pemetaan test case granular: TC-GS-ROLE-63, TC-GS-ROLE-66, TC-GS-ROLE-300, TC-GS-ROLE-304.
