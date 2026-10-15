---
id: TC-GS-GSET-E2E-038-security-derivasi-simbol-dan-payload-identik-no-op
title: "Security Payload: nilai simbol dari client diabaikan (di-derive dari Currency Code) dan PUT payload identik adalah no-op sukses"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-GSET-131
  - TC-GS-GSET-132
coverage:
  web: automated
---

# Security Payload: nilai simbol dari client diabaikan (di-derive dari Currency Code) dan PUT payload identik adalah no-op sukses

## Prerequisites

- Token sesi aktor Total Control tersedia untuk request API langsung ke `/v2/enterprise-management/general-settings`
- Record General Settings entitas tersimpan: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`
- `[simbol opsi USD]` = simbol yang tampil pada label opsi untuk kode USD

## Test Steps

### Simbol Di-derive dari Currency Code

1. Kirim PUT dengan currencyCode `USD`, currencySymbol `XX`, placement `suffix`, field lain sama dengan nilai tersimpan
2. Buka General Settings dan amati Preview Currency
3. Verifikasi Preview Currency "[simbol opsi USD] 5.000,00" (simbol dari `USD`, bukan `XX`; penempatan tidak berubah)
4. Verifikasi Currency Code `USD` tersimpan

### PUT Payload Identik No-Op

5. Catat jumlah baris Changelog
6. Kirim PUT dengan payload identik dengan nilai tersimpan
7. Verifikasi Response 200 tanpa toast netral di UI
8. Buka Modal Changelog dan Activity Log
9. Verifikasi jumlah baris Changelog dan Activity Log tidak bertambah (0 baris baru)

## Notes

- Spec FE+BE yang hanya mengasersi respons server dan state data. Menggabungkan TC-GS-GSET-131 dan 132.
